from django.http import HttpResponse

# imports to send confirmation emails
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import Profile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email.
        send_mail function called in handle_payment_intent_succeeded
        if order exists
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'golfmania_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # using intent to submit form even if user error occurs
        # user exits page during loading screen
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        order_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        # If username is not anon..get profile using username
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = Profile.objects.get(user__username=username)
            if save_info:
                profile.default_last_name = shipping_details.name
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address1 = \
                    shipping_details.address.line1
                profile.default_street_address2 = \
                    shipping_details.address.line2
                profile.default_town_city = shipping_details.address.city
                profile.default_county = shipping_details.address.state
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.save()

        # To check if order exists
        order_exists = False
        # if view is slow and data is not found in database,
        # delay is introduced to give time
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    last_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                # break while loop if order is found
                break

            except Order.DoesNotExist:
                # increment attempt by 1 to try find the order 5 times
                # in 5 seconds rather than just once
                attempt += 1
                time.sleep(1)
        if order_exists:
            # sending email if order exists
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | \
                    SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    last_name=shipping_details.name,
                    profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    town_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    # trying to find an order with the same basket items
                    # as well as payment_intent and try 5 times
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items(
                        ):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | \
                        ERROR: {e}', status=500)

        # sending email if order created by webhook handler
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | \
                SUCCESS: Created order in webhook', status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Payment Failed Webhook received: {event["type"]}',
            status=200)

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');


// Handle validation errors using event listener
// if error, it is displayed by creating an html snap
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('delivery-form');

form.addEventListener('submit', function(ev) {
    // when submit button clicked, form prevented from submitting
    ev.preventDefault();
    // submit btn set disabled once clicked and checked
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    // fading payment form and loading spinner overlay triggered after button is disabled
    $('#delivery-form').fadeToggle(100);
    $('#overlay-screen').fadeToggle(100);

    // capture all form data, especially the safe info check fieldset
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    
    var url = '/checkout/save_checkout_data/';

    // post form data to checkout view and if its valid
    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                // retrieve form data 
                billing_details: {
                    name: $.trim(form.last_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            // shipping excludes email and includes post code
            shipping: {
                name: $.trim(form.last_name.value),
                phone: $.trim(form.phone_number.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                // fading payment form and loading spinner overlay (2)
                $('#delivery-form').fadeToggle(100);
                $('#overlay-screen').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
        // if there is an error in the view, page reloads
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});
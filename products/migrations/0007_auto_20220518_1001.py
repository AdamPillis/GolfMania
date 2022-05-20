# Generated by Django 3.2 on 2022-05-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_old_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_hand',
        ),
        migrations.AddField(
            model_name='product',
            name='hand_type',
            field=models.CharField(blank=True, choices=[('Left Hand', 'Left Hand'), ('Right Hand', 'Right Hand')], default=False, max_length=20, null=True),
        ),
    ]
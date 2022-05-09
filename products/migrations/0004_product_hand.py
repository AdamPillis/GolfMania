# Generated by Django 3.2 on 2022-05-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hand',
            field=models.CharField(choices=[('Left Hand', 'Left Hand'), ('Right Hand', 'Right Hand')], default=False, max_length=20),
        ),
    ]
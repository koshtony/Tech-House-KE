# Generated by Django 5.1.2 on 2025-03-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_alter_orgprofile_fb_link_alter_orgprofile_ig_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbuild',
            name='disty_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

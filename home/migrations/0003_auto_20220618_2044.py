# Generated by Django 3.2.5 on 2022-06-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'PENDING'), (2, 'CONFIRMED'), (3, 'PACKED'), (4, 'SHIPPED'), (5, 'IN WAY'), (6, 'ARRIVED DESTINATION'), (7, 'RECIEVED'), (8, 'COMPLETED')], default=1),
        ),
    ]
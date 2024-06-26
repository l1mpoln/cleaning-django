# Generated by Django 4.2.7 on 2023-12-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_remove_profile_bio_remove_profile_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='INN',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='card_number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='enter',
            field=models.CharField(choices=[('O', 'Other option'), ('K', 'I will give a key'), ('H', 'I will be at home')], default='H', max_length=1),
        ),
    ]

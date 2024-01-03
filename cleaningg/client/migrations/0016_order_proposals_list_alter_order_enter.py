# Generated by Django 4.2.7 on 2023-12-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_alter_order_enter'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='proposals_list',
            field=models.ManyToManyField(blank=True, related_name='orders', to='client.proposal'),
        ),
        migrations.AlterField(
            model_name='order',
            name='enter',
            field=models.CharField(choices=[('O', 'Other option'), ('K', 'I will give a key'), ('H', 'I will be at home')], default='H', max_length=1),
        ),
    ]

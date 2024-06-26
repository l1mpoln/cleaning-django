# Generated by Django 4.2.7 on 2023-12-14 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_profile_is_cleaner_alter_order_enter_cleanerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_taken',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='proposals',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='enter',
            field=models.CharField(choices=[('H', 'I will be at home'), ('K', 'I will give a key'), ('O', 'Other option')], default='H', max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.package'),
        ),
    ]

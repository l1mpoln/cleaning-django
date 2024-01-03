# Generated by Django 4.2.7 on 2023-12-13 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0006_profile_inn_profile_card_number_alter_order_enter'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_cleaner',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='enter',
            field=models.CharField(choices=[('K', 'I will give a key'), ('O', 'Other option'), ('H', 'I will be at home')], default='H', max_length=1),
        ),
        migrations.CreateModel(
            name='CleanerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('reason_for_leaving', models.TextField(blank=True, null=True)),
                ('previous_work_experience', models.BooleanField(default=False)),
                ('punctuality', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('stress_resilience', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('cleaning_speed', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('cleaning_quality', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('willing_to_work_in_team', models.BooleanField(default=False)),
                ('own_cleaning_equipment', models.BooleanField(default=False)),
                ('city', models.CharField(blank=True, choices=[('Lviv', 'Lviv'), ('Kiyv', 'Kiyv'), ('Odessa', 'Odessa')], max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20240116_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='swiftapplication',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
    ]

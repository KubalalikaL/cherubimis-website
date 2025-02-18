# Generated by Django 5.1.6 on 2025-02-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('business_email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=200)),
                ('state_region', models.CharField(blank=True, max_length=100, null=True)),
                ('country_region', models.CharField(blank=True, max_length=100, null=True)),
                ('inquiry', models.TextField()),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

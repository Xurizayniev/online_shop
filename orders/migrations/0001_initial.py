# Generated by Django 4.0.6 on 2022-09-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=125)),
                ('address1', models.TextField(max_length=255)),
                ('address2', models.TextField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]

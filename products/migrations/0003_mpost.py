# Generated by Django 2.1 on 2019-06-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='mpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image_url', models.CharField(max_length=2083)),
                ('text', models.CharField(max_length=50000)),
            ],
        ),
    ]
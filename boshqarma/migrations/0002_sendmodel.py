# Generated by Django 4.0.3 on 2022-07-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boshqarma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('mavzu', models.CharField(max_length=100, null=True)),
                ('xabar', models.TextField(null=True)),
            ],
        ),
    ]

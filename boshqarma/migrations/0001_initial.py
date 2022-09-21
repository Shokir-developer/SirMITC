# Generated by Django 4.0.3 on 2022-07-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('body', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='%Y/%m/%d')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

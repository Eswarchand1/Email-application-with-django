# Generated by Django 4.0.3 on 2022-03-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0002_sendmsg'),
    ]

    operations = [
        migrations.CreateModel(
            name='receiveMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivemail', models.EmailField(max_length=254)),
                ('receivesubject', models.CharField(max_length=300)),
                ('receivetext', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0012_alter_walletbalance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getprofiledata',
            name='ppass',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='getprofiledata',
            name='prpass',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
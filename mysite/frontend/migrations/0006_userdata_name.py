# Generated by Django 3.1.3 on 2020-12-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20201203_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='name',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
# Generated by Django 4.1.1 on 2022-09-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='texto',
            name='resumo',
            field=models.TextField(null=True),
        ),
    ]

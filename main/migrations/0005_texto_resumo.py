# Generated by Django 4.1.1 on 2022-10-01 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_texto_resumo'),
    ]

    operations = [
        migrations.AddField(
            model_name='texto',
            name='resumo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
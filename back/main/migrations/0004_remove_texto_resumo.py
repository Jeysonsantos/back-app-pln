# Generated by Django 4.1.1 on 2022-09-30 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_texto_resumo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='texto',
            name='resumo',
        ),
    ]
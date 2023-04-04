# Generated by Django 4.1.7 on 2023-03-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_document_auditor_alter_document_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='permission',
            field=models.ManyToManyField(related_name='permission', through='app.UserPermission', to='app.permission'),
        ),
    ]

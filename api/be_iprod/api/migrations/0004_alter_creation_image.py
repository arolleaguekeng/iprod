# Generated by Django 4.1.5 on 2023-01-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_creation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creation',
            name='image',
            field=models.TextField(),
        ),
    ]

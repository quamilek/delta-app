# Generated by Django 4.2.3 on 2024-03-06 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_projectelement_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectelement',
            name='ref',
            field=models.CharField(max_length=255),
        ),
    ]

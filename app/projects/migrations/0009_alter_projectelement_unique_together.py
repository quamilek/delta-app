# Generated by Django 4.2.3 on 2024-03-06 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_projectelement_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='projectelement',
            unique_together={('project_name', 'ref', 'tq_pr')},
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Advanced')]),
        ),
    ]
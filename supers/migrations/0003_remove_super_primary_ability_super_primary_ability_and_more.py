# Generated by Django 4.0.3 on 2022-04-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_power'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='primary_ability',
        ),
        migrations.AddField(
            model_name='super',
            name='primary_ability',
            field=models.ManyToManyField(related_name='+', to='supers.power'),
        ),
        migrations.RemoveField(
            model_name='super',
            name='secondary_ability',
        ),
        migrations.AddField(
            model_name='super',
            name='secondary_ability',
            field=models.ManyToManyField(related_name='+', to='supers.power'),
        ),
    ]
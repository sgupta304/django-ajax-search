# Generated by Django 2.2.1 on 2019-05-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='release_groups',
            field=models.ManyToManyField(null=True, to='core.MusicRelease'),
        ),
    ]

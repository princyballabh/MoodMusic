# Generated by Django 4.0.3 on 2022-12-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0010_alter_song_copyrights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='copyrights',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

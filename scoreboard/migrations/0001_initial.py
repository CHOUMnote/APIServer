# Generated by Django 4.2 on 2023-05-29 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('clip', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
    ]

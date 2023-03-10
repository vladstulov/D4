# Generated by Django 4.1.6 on 2023-02-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('text', models.TextField()),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]

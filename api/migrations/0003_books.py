# Generated by Django 3.2.8 on 2021-10-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('bookId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]

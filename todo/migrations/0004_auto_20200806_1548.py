# Generated by Django 3.0.8 on 2020-08-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='memo',
            field=models.TextField(blank=True, default='No Memo added'),
        ),
    ]

# Generated by Django 4.1 on 2022-09-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse_habr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='id',
        ),
        migrations.AlterField(
            model_name='articles',
            name='link',
            field=models.CharField(max_length=4000, primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chessboard',
            name='personToMove',
            field=models.CharField(default='black', max_length=8),
        ),
    ]

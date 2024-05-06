# Generated by Django 4.2.11 on 2024-05-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='user',
        ),
        migrations.AddField(
            model_name='wallet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='userId',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

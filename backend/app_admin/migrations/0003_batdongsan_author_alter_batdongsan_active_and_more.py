# Generated by Django 5.1.4 on 2025-02-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0002_batdongsan_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='batdongsan',
            name='author',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='batdongsan',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='batdongsan',
            name='information',
            field=models.TextField(verbose_name=''),
        ),
    ]

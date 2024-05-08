# Generated by Django 5.0.4 on 2024-05-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Book Title')),
                ('description', models.TextField(max_length=500, verbose_name='Book Description')),
                ('rate', models.PositiveBigIntegerField(verbose_name='Book Rate')),
                ('views', models.PositiveBigIntegerField(verbose_name='Book Views')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
    ]
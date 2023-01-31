# Generated by Django 4.1.4 on 2023-01-31 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50, unique=True)),
                ('course_price', models.CharField(max_length=10)),
                ('course_length', models.CharField(max_length=20)),
                ('course_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Teachers',
            new_name='Teacher',
        ),
    ]
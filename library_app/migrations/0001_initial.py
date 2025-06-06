# Generated by Django 5.0.6 on 2024-05-23 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=40)),
                ('publisher_name', models.CharField(max_length=30)),
                ('pub_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=40)),
                ('user_number', models.CharField(max_length=15)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_dob', models.DateField()),
                ('user_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=40)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book')),
            ],
        ),
        migrations.CreateModel(
            name='Book_issued',
            fields=[
                ('book_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='library_app.book')),
                ('date_out', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.user')),
            ],
        ),
    ]

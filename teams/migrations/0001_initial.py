# Generated by Django 4.1.3 on 2022-12-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('titles', models.IntegerField(default=0)),
                ('top_scorer', models.CharField(max_length=50)),
                ('fifa_code', models.CharField(max_length=3, unique=True)),
                ('founded_at', models.DateField()),
            ],
        ),
    ]

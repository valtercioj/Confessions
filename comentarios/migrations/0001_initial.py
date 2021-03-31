# Generated by Django 3.1.6 on 2021-03-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('confissions', models.TextField(max_length=400)),
                ('datetime', models.TimeField(auto_now=True)),
            ],
        ),
    ]
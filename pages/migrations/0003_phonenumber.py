# Generated by Django 2.2.7 on 2019-11-17 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phonenumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('created', models.DateTimeField(verbose_name='data created')),
                ('firstname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Firstname')),
            ],
        ),
    ]

# Generated by Django 2.0.3 on 2018-04-12 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='itzc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jqm', models.CharField(max_length=20)),
                ('ipaddr', models.CharField(max_length=35)),
                ('user', models.CharField(max_length=35)),
                ('userpwd', models.CharField(max_length=35)),
                ('addr', models.CharField(max_length=45)),
                ('paydate', models.CharField(max_length=35)),
            ],
        ),
    ]

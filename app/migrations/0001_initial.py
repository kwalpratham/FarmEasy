# Generated by Django 4.0 on 2022-05-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='landModel',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('ownerName', models.CharField(max_length=50)),
                ('irrigationSource', models.CharField(default='', max_length=500)),
                ('climateCond', models.CharField(default='', max_length=500)),
                ('cropHistory', models.CharField(default='', max_length=5000)),
                ('address', models.CharField(default='', max_length=5000)),
                ('landSize', models.CharField(default='', max_length=500)),
                ('soilType', models.CharField(default='', max_length=5000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]

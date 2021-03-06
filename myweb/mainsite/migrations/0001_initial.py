# Generated by Django 2.0.3 on 2018-04-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.FloatField()),
                ('sepal_width', models.FloatField()),
                ('petal_length', models.FloatField()),
                ('petal_width', models.FloatField()),
                ('species', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('species',),
            },
        ),
    ]

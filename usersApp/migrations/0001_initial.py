# Generated by Django 4.1.4 on 2022-12-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('postcode', models.IntegerField(default=0)),
                ('country', models.CharField(choices=[('UK', 'UK'), ('Argentina', 'Argentina'), ('portugal', 'portugal'), ('India', 'India'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='UK', max_length=20)),
            ],
        ),
    ]

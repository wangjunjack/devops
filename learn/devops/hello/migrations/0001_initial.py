# Generated by Django 2.2 on 2021-04-13 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='用户名', max_length=20)),
                ('password', models.CharField(help_text='密码', max_length=32)),
                ('sex', models.IntegerField(blank=True, choices=[('0', '男'), ('1', '女')], null=True)),
            ],
        ),
    ]

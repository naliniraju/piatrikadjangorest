# Generated by Django 2.2 on 2019-04-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ryot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ryotcode', models.CharField(default='', max_length=70)),
                ('ryotname', models.CharField(default='', max_length=70)),
                ('grouprefno', models.CharField(default='', max_length=70)),
                ('fwgname', models.CharField(default='', max_length=70)),
                ('villagecode', models.CharField(default='', max_length=70)),
                ('villagename', models.CharField(default='', max_length=70)),
                ('mandalcode', models.CharField(default='', max_length=70)),
                ('mandalname', models.CharField(default='', max_length=70)),
                ('csicode', models.CharField(default='', max_length=70)),
                ('csiname', models.CharField(default='', max_length=70)),
                ('sectioncode', models.CharField(default='', max_length=70)),
                ('sectionname', models.CharField(default='', max_length=70)),
                ('literarystatus', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('address1', models.CharField(default='', max_length=70)),
                ('address2', models.CharField(default='', max_length=70)),
                ('city', models.CharField(default='', max_length=70)),
                ('paymode', models.CharField(default='', max_length=70)),
                ('landno', models.CharField(default='', max_length=70)),
                ('mobileno', models.CharField(default='', max_length=70)),
                ('bankcode', models.CharField(default='', max_length=70)),
                ('bankname', models.CharField(default='', max_length=70)),
                ('sbacno', models.CharField(default='', max_length=70)),
                ('loanacno', models.CharField(default='', max_length=70)),
                ('ledgerno', models.CharField(default='', max_length=70)),
                ('loanaccountledgerno', models.CharField(default='', max_length=70)),
                ('foliono', models.CharField(default='', max_length=70)),
                ('loanacfoliono', models.CharField(default='', max_length=70)),
            ],
        ),
    ]

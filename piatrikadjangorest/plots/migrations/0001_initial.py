# Generated by Django 2.2 on 2019-04-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(default='', max_length=70)),
                ('csi', models.CharField(default='', max_length=70)),
                ('section', models.CharField(default='', max_length=70)),
                ('offerno', models.CharField(default='', max_length=70)),
                ('offerdate', models.DateField(blank=True, null=True)),
                ('planteddate', models.DateField(blank=True, null=True)),
                ('plottype', models.CharField(default='', max_length=70)),
                ('plotno', models.CharField(default='', max_length=70)),
                ('ryot', models.CharField(default='', max_length=70)),
                ('village', models.CharField(default='', max_length=70)),
                ('rationtype', models.CharField(default='', max_length=70)),
                ('agreementacre', models.CharField(default='', max_length=70)),
                ('agreementedtonne', models.CharField(default='', max_length=70)),
                ('measuredarea', models.CharField(default='', max_length=70)),
                ('guarantor1', models.CharField(default='', max_length=70)),
                ('guarantor2', models.CharField(default='', max_length=70)),
                ('guarantorname', models.CharField(default='', max_length=70)),
            ],
        ),
    ]

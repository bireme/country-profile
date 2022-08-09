# Generated by Django 4.0.7 on 2022-08-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_domain_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryindicatordata',
            name='reference_number',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Reference #'),
        ),
        migrations.AlterField(
            model_name='countryindicatordata',
            name='reference',
            field=models.TextField(blank=True, verbose_name='Reference'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='number',
            field=models.SmallIntegerField(verbose_name='Domain number'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='code',
            field=models.CharField(max_length=25, unique=True, verbose_name='Code'),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-09 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_auto_20191009_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trialbalance',
            name='beginningBalance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trialbalance',
            name='endingBalance',
            field=models.FloatField(),
        ),
    ]
# Generated by Django 3.1.6 on 2021-02-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20210211_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='portfolio_site',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.2 on 2020-08-06 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CBTS_APP', '0004_auto_20200806_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='compositeobjective',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CBTS_APP.Subject'),
        ),
    ]

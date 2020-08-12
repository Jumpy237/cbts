# Generated by Django 3.0.2 on 2020-08-06 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CBTS_APP', '0003_auto_20200806_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compositeobjective',
            name='cnt',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CBTS_APP.CompositeObjective'),
        ),
    ]

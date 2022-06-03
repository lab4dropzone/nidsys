# Generated by Django 4.0.3 on 2022-06-03 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nidsys', '0002_previousaddr'),
    ]

    operations = [
        migrations.AddField(
            model_name='previousaddr',
            name='fromdate',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='previousaddr',
            name='prevaddr',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='previousaddr',
            name='regid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='nidsys.registration'),
        ),
        migrations.AddField(
            model_name='previousaddr',
            name='todate',
            field=models.TextField(default=None),
        ),
    ]
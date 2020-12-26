# Generated by Django 3.1.2 on 2020-12-14 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201214_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]

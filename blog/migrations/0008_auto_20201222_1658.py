# Generated by Django 3.1.2 on 2020-12-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201222_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenter',
            name='username',
            field=models.CharField(default='Anonymoux', max_length=100),
            preserve_default=False,
        ),
    ]

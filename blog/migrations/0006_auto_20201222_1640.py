# Generated by Django 3.1.2 on 2020-12-22 15:40

from django.conf import settings
import django.contrib.auth.mixins
from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.edit


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20201215_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCreate',
            fields=[
                ('commenter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.commenter')),
            ],
            bases=(django.contrib.auth.mixins.LoginRequiredMixin, django.views.generic.edit.CreateView, 'blog.commenter'),
        ),
        migrations.AlterField(
            model_name='commenter',
            name='username',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

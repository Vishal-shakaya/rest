# Generated by Django 3.0.7 on 2020-06-07 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=233)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('user_feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
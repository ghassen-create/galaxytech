# Generated by Django 4.2.2 on 2023-07-09 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='work_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.workgroup'),
        ),
    ]

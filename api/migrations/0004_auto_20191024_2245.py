# Generated by Django 2.2.6 on 2019-10-24 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191023_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodulemodel',
            name='module_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AddConstraint(
            model_name='gamelevelmodel',
            constraint=models.UniqueConstraint(fields=('level_number', 'module'), name='unique_level_in_module'),
        ),
        migrations.AddConstraint(
            model_name='usergamelevelmodel',
            constraint=models.UniqueConstraint(fields=('user', 'game_level'), name='unique_user_level'),
        ),
        migrations.AddConstraint(
            model_name='usergamemodulemodel',
            constraint=models.UniqueConstraint(fields=('user', 'game_module'), name='unique_user_module'),
        ),
    ]

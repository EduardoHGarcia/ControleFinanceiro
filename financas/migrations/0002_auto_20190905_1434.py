# Generated by Django 2.2.5 on 2019-09-05 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='is_deletado',
            field=models.BooleanField(default=False),
        ),
    ]

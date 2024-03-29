# Generated by Django 2.2.5 on 2019-09-05 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Forma_Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Forma Pagamento',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tipo Transações',
            },
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=250)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dt_transacao', models.DateTimeField()),
                ('is_deletado', models.BooleanField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financas.Categoria')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financas.Conta')),
                ('forma_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financas.Forma_Pagamento')),
                ('tipo_transacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financas.Tipo_Transacao')),
            ],
            options={
                'verbose_name_plural': 'Transações',
            },
        ),
    ]

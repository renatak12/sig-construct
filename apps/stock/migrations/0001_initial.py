# Generated by Django 4.2.3 on 2023-07-22 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.IntegerField(default=0)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produtos/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.categoria')),
                ('fornecedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('forma_pagamento', models.CharField(max_length=20)),
                ('parcelamento', models.IntegerField(blank=True, null=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_total_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.produto')),
            ],
        ),
    ]

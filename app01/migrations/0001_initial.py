# Generated by Django 4.1.4 on 2023-07-20 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cutter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('supplier', models.CharField(max_length=128, null=True)),
                ('minHoleTole', models.CharField(max_length=128, null=True)),
                ('maxHoleTole', models.CharField(max_length=128, null=True)),
                ('minDia', models.CharField(max_length=128, null=True)),
                ('maxDia', models.CharField(max_length=128, null=True)),
                ('minDepDia', models.CharField(max_length=128, null=True)),
                ('maxDepDia', models.CharField(max_length=128, null=True)),
                ('capMat', models.TextField(null=True)),
                ('cutterMat', models.CharField(max_length=128, null=True)),
                ('capPro', models.TextField(null=True)),
                ('cutterCost', models.CharField(max_length=128, null=True)),
                ('cutterImg', models.TextField(null=True)),
                ('cutterRemark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('classFirst', models.CharField(max_length=128)),
                ('classSecond', models.CharField(max_length=128, null=True)),
                ('paraDef', models.TextField(null=True)),
                ('imgPath', models.TextField(null=True)),
                ('remark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManuCapRule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, null=True, unique=True)),
                ('captype', models.CharField(max_length=128, null=True)),
                ('manuType', models.CharField(max_length=128, null=True)),
                ('featType1', models.CharField(max_length=128, null=True)),
                ('featType2', models.CharField(max_length=128, null=True)),
                ('featPro', models.CharField(max_length=128, null=True)),
                ('resType', models.CharField(max_length=128, null=True)),
                ('content', models.TextField(null=True)),
                ('script', models.TextField(null=True)),
                ('inputParaList', models.TextField(null=True)),
                ('outputParaList', models.TextField(null=True)),
                ('paraTable', models.CharField(max_length=128, null=True)),
                ('ManuCapRemark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('addr', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, null=True, unique=True)),
                ('ruleTypeFirst', models.CharField(max_length=128, null=True)),
                ('ruleTypeSecond', models.CharField(max_length=128, null=True)),
                ('manuType', models.CharField(max_length=128, null=True)),
                ('featTypeFirst', models.CharField(max_length=128, null=True)),
                ('featTypeSecond', models.CharField(max_length=128, null=True)),
                ('featPro', models.CharField(max_length=128, null=True)),
                ('content', models.TextField(null=True)),
                ('imgPath', models.TextField(null=True)),
                ('script', models.TextField(null=True)),
                ('remark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TableFunction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('functionName', models.CharField(max_length=128, null=True, unique=True)),
                ('inputPara', models.TextField(null=True)),
                ('outputPara', models.TextField(null=True)),
                ('sql', models.TextField(null=True)),
                ('remark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeParaTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('paraType', models.CharField(max_length=128, null=True)),
                ('defaultValue', models.TextField(null=True)),
                ('remark', models.TextField(null=True)),
                ('ruleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.manucaprule')),
                ('tableFunction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.tablefunction', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('book', models.ManyToManyField(to='app01.book')),
            ],
        ),
    ]

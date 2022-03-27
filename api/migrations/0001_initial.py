# Generated by Django 4.0.3 on 2022-03-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosisCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(choices=[('icd-9', 'ICD-9 2012'), ('icd-10', 'ICD-10 2022'), ('icd-11', 'ICD-11 2022')], default='icd-10', max_length=20)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('title',),
            },
        ),
    ]
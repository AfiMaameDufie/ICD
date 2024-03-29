# Generated by Django 4.0.3 on 2022-03-27 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis_code', models.CharField(blank=True, default='', max_length=10)),
                ('full_code', models.CharField(max_length=20)),
                ('abbreviation_description', models.CharField(max_length=500)),
                ('full_description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to='api.diagnosiscategory')),
            ],
            options={
                'ordering': ('full_code',),
            },
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-08 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(default='', max_length=300)),
                ('content', models.CharField(default='', max_length=3000)),
                ('kind', models.CharField(blank=True, choices=[('facility_bene', '시설 관련'), ('food_bene', '음식점 관련'), ('shopping_bene', '쇼핑 관련')], max_length=20, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='benefits', to='categories.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

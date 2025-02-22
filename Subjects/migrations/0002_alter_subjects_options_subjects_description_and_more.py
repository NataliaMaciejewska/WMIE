# Generated by Django 4.2.1 on 2023-10-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subjects',
            options={'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects'},
        ),
        migrations.AddField(
            model_name='subjects',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='field_of_study',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subjects',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subjects',
            name='specialization',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='counter',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

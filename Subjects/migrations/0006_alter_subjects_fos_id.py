# Generated by Django 4.2.1 on 2024-01-16 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0005_fos_remove_subjects_field_of_study_subjects_fos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='FOS_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Subjects.fos'),
        ),
    ]

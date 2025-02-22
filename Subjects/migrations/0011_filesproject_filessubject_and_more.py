# Generated by Django 4.2.1 on 2024-01-16 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0010_projects_rename_fos_fieldsofstudy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(blank=True, null=True, unique=True, upload_to='uploads/')),
                ('counter', models.IntegerField(blank=True, default=0)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Subjects.projects')),
            ],
            options={
                'verbose_name': 'FileProject',
                'verbose_name_plural': 'FilesProjects',
            },
        ),
        migrations.CreateModel(
            name='FilesSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(blank=True, null=True, unique=True, upload_to='uploads/')),
                ('counter', models.IntegerField(blank=True, default=0)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Subjects.subjects')),
            ],
            options={
                'verbose_name': 'FileSubject',
                'verbose_name_plural': 'FilesSubject',
            },
        ),
        migrations.AlterModelOptions(
            name='fieldsofstudy',
            options={'verbose_name': 'FieldOfStudy', 'verbose_name_plural': 'FieldsOfStudy'},
        ),
        migrations.DeleteModel(
            name='Files',
        ),
    ]

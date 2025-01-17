# Generated by Django 5.1.5 on 2025-01-17 13:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='passing_score',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='questions',
        ),
        migrations.AddField(
            model_name='assignment',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name_en',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name_ru',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='documents',
            field=models.ImageField(default=1, upload_to='lesson_file/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_en',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_ru',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='option',
            name='text_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='option',
            name='text_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passing_score', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('duration', models.DurationField(verbose_name=60)),
                ('Questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_questions', to='app_course.exam')),
            ],
        ),
    ]

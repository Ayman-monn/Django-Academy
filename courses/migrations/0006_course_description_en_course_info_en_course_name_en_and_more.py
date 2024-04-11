# Generated by Django 5.0.3 on 2024-03-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_comment_options_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description_en'),
        ),
        migrations.AddField(
            model_name='course',
            name='info_en',
            field=models.TextField(blank=True, null=True, verbose_name='Info_en'),
        ),
        migrations.AddField(
            model_name='course',
            name='name_en',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Name_en'),
        ),
        migrations.AddField(
            model_name='course',
            name='short_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Short_description_en'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='description_en',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='name_en',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='section',
            name='name_en',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Name_en'),
        ),
        migrations.AddField(
            model_name='studentcourses',
            name='amount_paid',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.5 on 2022-03-23 11:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datainfo', '0004_question_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

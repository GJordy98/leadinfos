# Generated by Django 5.0.3 on 2024-04-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contenu',
            field=models.TextField(default='Contenu'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'DRAFT'), (1, 'PUBLISHED')], default=0),
        ),
    ]

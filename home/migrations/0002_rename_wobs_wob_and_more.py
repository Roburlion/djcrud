# Generated by Django 5.1.7 on 2025-03-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WOBs',
            new_name='WOB',
        ),
        migrations.RenameIndex(
            model_name='wob',
            new_name='home_wob_batch_ca9f27_idx',
            old_name='home_wobs_batch_33a6d9_idx',
        ),
        migrations.AlterField(
            model_name='rollbatches',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rolls',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

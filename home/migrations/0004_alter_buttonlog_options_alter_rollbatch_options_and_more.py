# Generated by Django 5.1.7 on 2025-03-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_rollbatches_rollbatch_roll_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buttonlog',
            options={'verbose_name': 'Button Log', 'verbose_name_plural': 'Button Logs'},
        ),
        migrations.AlterModelOptions(
            name='rollbatch',
            options={'verbose_name': 'Roll Batch', 'verbose_name_plural': 'Roll Batches'},
        ),
        migrations.AlterModelOptions(
            name='wob',
            options={'verbose_name': 'WOB', 'verbose_name_plural': 'WOBs'},
        ),
        migrations.AlterField(
            model_name='rollbatch',
            name='batch',
            field=models.CharField(blank=True, default='', max_length=9),
        ),
    ]

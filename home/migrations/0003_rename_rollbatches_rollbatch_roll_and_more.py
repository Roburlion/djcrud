# Generated by Django 5.1.7 on 2025-03-15 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_wobs_wob_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RollBatches',
            new_name='RollBatch',
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='roll', to='home.workflow')),
            ],
        ),
        migrations.AlterField(
            model_name='rollbatch',
            name='roll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='roll_batches', to='home.roll'),
        ),
        migrations.DeleteModel(
            name='Rolls',
        ),
    ]

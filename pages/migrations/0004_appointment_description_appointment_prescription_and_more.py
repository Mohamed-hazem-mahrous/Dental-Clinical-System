# Generated by Django 4.1 on 2023-06-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_name_patient_fname_patient_lname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        # migrations.AddField(
        #     model_name='appointment',
        #     name='prescription',
        #     field=models.CharField(max_length=2000, null=True),
        # ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-08 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_attendance_education_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='attendance',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='home.attendance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='home.location'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='attendance',
            constraint=models.UniqueConstraint(fields=('start_date', 'end_date'), name='unique_attendance'),
        ),
        migrations.AddConstraint(
            model_name='location',
            constraint=models.UniqueConstraint(fields=('city', 'state'), name='unique_location'),
        ),
    ]
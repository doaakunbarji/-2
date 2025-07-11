# Generated by Django 5.2.1 on 2025-05-28 16:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_medication_end_date_medication_start_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="labrequest",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lab_requests",
                to="core.patient",
            ),
        ),
        migrations.AlterField(
            model_name="labrequest",
            name="request_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="labrequest",
            name="request_type",
            field=models.CharField(
                choices=[("تحليل", "تحليل"), ("أشعة", "أشعة")], max_length=20
            ),
        ),
        migrations.AlterField(
            model_name="labrequest",
            name="status",
            field=models.CharField(default="قيد التنفيذ", max_length=50),
        ),
    ]

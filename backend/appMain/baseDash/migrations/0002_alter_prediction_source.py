# Generated by Django 4.1.3 on 2022-11-17 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseDash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry', to='baseDash.profile'),
        ),
    ]
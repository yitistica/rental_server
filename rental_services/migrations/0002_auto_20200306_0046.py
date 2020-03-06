# Generated by Django 3.0.3 on 2020-03-05 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalunit',
            name='rental_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='rental_services.Owner'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='given_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nid_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='manager',
            name='given_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='manager',
            name='nid_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='manager',
            name='surname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='owner',
            name='given_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='owner',
            name='nid_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='owner',
            name='surname',
            field=models.CharField(max_length=20),
        ),
    ]

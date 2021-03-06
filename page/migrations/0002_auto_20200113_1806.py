# Generated by Django 3.0.2 on 2020-01-13 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.TextField()),
                ('tracking_number', models.CharField(max_length=12)),
                ('serial_pin', models.CharField(max_length=6)),
                ('route', models.IntegerField(choices=[(1, 'Air'), (2, 'Sea'), (3, 'Land')])),
                ('initial_transit', models.CharField(max_length=100)),
                ('current_transit', models.CharField(max_length=100)),
                ('next_transit', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Users')),
            ],
        ),
    ]

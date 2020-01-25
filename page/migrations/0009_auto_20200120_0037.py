# Generated by Django 3.0.2 on 2020-01-20 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('page', '0008_comment_enquiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='current_transit',
        ),
        migrations.RemoveField(
            model_name='item',
            name='initial_transit',
        ),
        migrations.RemoveField(
            model_name='item',
            name='next_transit',
        ),
        migrations.AddField(
            model_name='item',
            name='transit',
            field=models.ManyToManyField(help_text='Add a transit for this item', to='dashboard.Transit'),
        ),
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postal',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_accounts_address_alter_accounts_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='lname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='zip',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
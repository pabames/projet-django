# Generated by Django 4.0.3 on 2022-03-24 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.TextField()),
                ('image', models.FileField(max_length=255, null=True, upload_to='')),
                ('date', models.DateField(auto_now=True)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.FileField(max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.FileField(max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='design',
            name='image',
            field=models.FileField(max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='developpement',
            name='image',
            field=models.FileField(max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='visa',
            name='image',
            field=models.FileField(max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contact',
        ),
    ]

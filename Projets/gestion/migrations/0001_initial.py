# Generated by Django 4.1.11 on 2023-10-18 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('starting_date', models.DateField()),
                ('expected_ending_date', models.DateField()),
                ('statut', models.CharField(choices=[('en_cours', 'En Cours'), ('annulee', 'Annulée'), ('terminee', 'Terminée')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('role', models.TextField()),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link_to_file', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('starting_date', models.DateField()),
                ('expected_ending_date', models.DateField()),
                ('statut', models.CharField(choices=[('intouchee', 'Intouchée'), ('en_cours', 'En Cours'), ('annulee', 'Annulée'), ('terminee', 'Terminée')], max_length=15)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.project')),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('expected_date', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.project')),
            ],
        ),
    ]

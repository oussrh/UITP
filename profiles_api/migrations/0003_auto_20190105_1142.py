# Generated by Django 2.1.4 on 2019-01-05 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequence', models.IntegerField()),
                ('commentaire', models.TextField()),
                ('motivation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Incidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomIncident', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rapports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.IntegerField()),
                ('is_Done', models.BooleanField(default=False)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeIncidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomType', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='incidents',
            name='idTypeIncidents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.TypeIncidents'),
        ),
        migrations.AddField(
            model_name='detail',
            name='idIncidents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.Incidents'),
        ),
        migrations.AddField(
            model_name='detail',
            name='idRapport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.Rapports'),
        ),
        migrations.AddField(
            model_name='detail',
            name='idTransport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.Transports'),
        ),
    ]

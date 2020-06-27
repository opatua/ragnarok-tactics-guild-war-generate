# Generated by Django 2.2.13 on 2020-06-25 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ragnarok', '0006_historicalmonster_historicalmonsterelement_monster_monsterelement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essence',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('legendary', 'Legendary'), ('epic', 'Epic'), ('rare', 'Rare')], max_length=255)),
                ('element', models.CharField(choices=[('fire', 'Fire'), ('earth', 'Earth'), ('water', 'Water'), ('wind', 'Wind'), ('dark', 'Dark'), ('holy', 'Holy')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalEssence',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('legendary', 'Legendary'), ('epic', 'Epic'), ('rare', 'Rare')], max_length=255)),
                ('element', models.CharField(choices=[('fire', 'Fire'), ('earth', 'Earth'), ('water', 'Water'), ('wind', 'Wind'), ('dark', 'Dark'), ('holy', 'Holy')], max_length=255)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical essence',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
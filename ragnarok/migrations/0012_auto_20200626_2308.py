# Generated by Django 2.2.13 on 2020-06-26 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ragnarok', '0011_auto_20200626_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactionBoost',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='historicalmonster',
            name='type',
            field=models.CharField(choices=[('legendary', 'Legendary'), ('epic', 'Epic'), ('rare', 'Rare'), ('normal', 'Normal')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='type',
            field=models.CharField(choices=[('legendary', 'Legendary'), ('epic', 'Epic'), ('rare', 'Rare'), ('normal', 'Normal')], max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='HistoricalFactionBoostAttribute',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('faction', models.CharField(choices=[('rock', 'Rock'), ('paper', 'Paper'), ('scissor', 'Scissor'), ('white', 'White'), ('black', 'Black')], max_length=255)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('faction_boost', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ragnarok.FactionBoost')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical faction boost attribute',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFactionBoost',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical faction boost',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='FactionBoostAttribute',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('faction', models.CharField(choices=[('rock', 'Rock'), ('paper', 'Paper'), ('scissor', 'Scissor'), ('white', 'White'), ('black', 'Black')], max_length=255)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('faction_boost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ragnarok.FactionBoost')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
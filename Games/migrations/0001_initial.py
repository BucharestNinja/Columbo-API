# Generated by Django 2.1 on 2019-07-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deckName', models.CharField(max_length=40)),
                ('card1', models.CharField(max_length=50)),
                ('card2', models.CharField(max_length=50)),
                ('card3', models.CharField(max_length=50)),
                ('card4', models.CharField(max_length=50)),
                ('card5', models.CharField(max_length=50)),
                ('card6', models.CharField(max_length=50)),
                ('card7', models.CharField(max_length=50)),
                ('card8', models.CharField(max_length=50)),
                ('card9', models.CharField(max_length=50)),
                ('card10', models.CharField(max_length=50)),
                ('card11', models.CharField(max_length=50)),
                ('card12', models.CharField(max_length=50)),
                ('card13', models.CharField(max_length=50)),
                ('card14', models.CharField(max_length=50)),
                ('card15', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'deck',
            },
        ),
    ]

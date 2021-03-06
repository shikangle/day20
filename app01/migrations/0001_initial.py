# Generated by Django 2.0.7 on 2018-07-18 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(db_index=True, max_length=32)),
                ('ip', models.GenericIPAddressField(db_index=True)),
                ('b', models.ForeignKey(on_delete=True, to='app01.Business')),
            ],
        ),
    ]

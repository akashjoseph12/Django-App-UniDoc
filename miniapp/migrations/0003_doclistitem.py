# Generated by Django 4.0.3 on 2022-12-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0002_appointment_delete_doclistitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('dateof', models.DateField()),
            ],
        ),
    ]

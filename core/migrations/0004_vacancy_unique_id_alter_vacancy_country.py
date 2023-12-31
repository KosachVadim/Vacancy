# Generated by Django 4.2.5 on 2023-09-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_vacancy_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='unique_id',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='country',
            field=models.CharField(choices=[('Польша(pl)', 'Польша(pl)'), ('Германия(de)', 'Германия(de)'), ('Литва(lt)', 'Литва(lt)'), ('Испания(es)', 'Испания(es)'), ('Бельгия(be)', 'Бельгия(be)'), ('Великобритания(uk)', 'Великобритания(uk)')], max_length=255),
        ),
    ]

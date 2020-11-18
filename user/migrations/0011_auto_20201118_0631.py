# Generated by Django 3.1.3 on 2020-11-18 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_remove_district_district_categories'),
        ('user', '0010_user_recomender'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user_carrer_filter',
            table='user_carrer_filters',
        ),
        migrations.CreateModel(
            name='User_district_filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.district')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_district_filters',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='district_filter',
            field=models.ManyToManyField(related_name='user_districts_filters', through='user.User_district_filter', to='company.District'),
        ),
    ]
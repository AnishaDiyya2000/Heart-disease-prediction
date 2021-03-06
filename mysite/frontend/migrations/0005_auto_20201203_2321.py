# Generated by Django 3.1.3 on 2020-12-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_add_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='addData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (0, 'Female')])),
                ('cp', models.IntegerField(choices=[(0, 'ATYPICAL ANGINA'), (1, 'TYPICAL ANGINA'), (2, 'ASYMPTOMATIC'), (3, 'NON ANGINAL PAIN')])),
                ('testbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField(choices=[(0, 'FALSE'), (1, 'TRUE')])),
                ('restecg', models.IntegerField(choices=[(0, 'NORMAL'), (1, 'HAVING ST-T'), (2, 'HYPERTROPHY')])),
                ('thalch', models.IntegerField()),
                ('exang', models.IntegerField(choices=[(1, 'YES'), (0, 'N0')])),
                ('oldpeak', models.FloatField()),
                ('slope', models.IntegerField(choices=[(1, 'UP_SLOPING'), (2, 'FLAT'), (3, 'DOWN_SLOPING')])),
                ('ca', models.IntegerField()),
                ('thal', models.IntegerField(choices=[(3, 'NORMAL'), (6, 'FIXED DEFECT'), (7, 'REVERSIBLE DEFECT')])),
            ],
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='sex',
        ),
    ]

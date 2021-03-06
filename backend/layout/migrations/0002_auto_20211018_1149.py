# Generated by Django 3.2.8 on 2021-10-18 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tables',
            options={'ordering': ('title',), 'verbose_name_plural': 'Tables'},
        ),
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_title', models.CharField(max_length=254)),
                ('machine_os', models.CharField(max_length=254)),
                ('machine_ip_address', models.CharField(max_length=254)),
                ('machine_user_name', models.CharField(max_length=254)),
                ('numbers_of_gpu', models.IntegerField()),
                ('slug', models.SlugField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computerTable', to='layout.tables')),
            ],
            options={
                'verbose_name_plural': 'Computers',
                'ordering': ('-date_added',),
            },
        ),
    ]

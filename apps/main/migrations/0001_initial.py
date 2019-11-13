# Generated by Django 2.2.6 on 2019-11-12 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('bro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Bro')),
            ],
        ),
        migrations.CreateModel(
            name='Shout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Bro')),
                ('expression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Expression')),
            ],
        ),
    ]

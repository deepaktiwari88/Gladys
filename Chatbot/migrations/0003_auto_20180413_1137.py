# Generated by Django 2.0.3 on 2018-04-13 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatbot', '0002_auto_20180409_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('message', models.TextField(max_length=200)),
                ('isuser', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='house_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='shop_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_item', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listitem',
            options={'verbose_name': 'Элемент списка', 'verbose_name_plural': 'Элементы списка'},
        ),
        migrations.AlterField(
            model_name='listitem',
            name='expare_date',
            field=models.DateTimeField(null=True),
        ),
    ]

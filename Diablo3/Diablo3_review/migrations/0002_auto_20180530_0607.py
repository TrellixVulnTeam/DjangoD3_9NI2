# Generated by Django 2.0.2 on 2018-05-30 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diablo3_review', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Catégorie', 'verbose_name_plural': 'Catégories'},
        ),
        migrations.AddField(
            model_name='myarticle',
            name='description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
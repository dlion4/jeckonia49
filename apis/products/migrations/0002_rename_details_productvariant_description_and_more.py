# Generated by Django 4.2.7 on 2024-03-15 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariant',
            old_name='details',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]

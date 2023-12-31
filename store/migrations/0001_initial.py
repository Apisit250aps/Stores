# Generated by Django 4.2.6 on 2023-10-19 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=128)),
                ('area_code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=8, null=True, unique=True)),
                ('product_name', models.CharField(max_length=255)),
                ('product_desc', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTypeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=128, unique=True)),
                ('product_type_code', models.CharField(max_length=8, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_code', models.CharField(max_length=8, null=True, unique=True)),
                ('shop_name', models.CharField(max_length=128)),
                ('shop_contact', models.CharField(max_length=255)),
                ('shop_address', models.TextField()),
                ('shop_sub_district', models.CharField(max_length=128)),
                ('shop_district', models.CharField(max_length=128)),
                ('shop_province', models.CharField(max_length=128)),
                ('shop_zip', models.CharField(max_length=5)),
                ('shop_tel', models.CharField(max_length=10)),
                ('shop_fax', models.CharField(max_length=10)),
                ('shop_email', models.EmailField(max_length=254)),
                ('shop_remark', models.TextField()),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.producttypedata')),
                ('shop_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.areadata')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_unit', models.IntegerField()),
                ('delete_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productdata')),
            ],
        ),
        migrations.AddField(
            model_name='productdata',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shopdata'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.producttypedata'),
        ),
        migrations.CreateModel(
            name='InputInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=10, unique=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('remark', models.TextField()),
                ('input_date', models.DateTimeField(auto_now_add=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shopdata')),
            ],
        ),
        migrations.CreateModel(
            name='InputData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.inputinvoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productdata')),
            ],
        ),
    ]

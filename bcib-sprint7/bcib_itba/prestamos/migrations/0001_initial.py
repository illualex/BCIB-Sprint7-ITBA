# Generated by Django 4.2.7 on 2023-12-04 01:01

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
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.TextField()),
                ('loan_date', models.TextField()),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'prestamo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cliente', models.CharField(choices=[('BLACK', 'BLACK'), ('GOLD', 'GOLD'), ('CLASSIC', 'CLASSIC')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPrestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('monto_maximo', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudPrestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('monto_solicitado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('aprobado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.cliente')),
                ('tipo_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.tipoprestamo')),
            ],
        ),
    ]

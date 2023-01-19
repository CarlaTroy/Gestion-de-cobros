# Generated by Django 4.1.2 on 2022-12-31 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('dues_number', models.PositiveIntegerField(verbose_name='Cuotas')),
                ('initial_payment', models.FloatField(default=0, verbose_name='Pago Inicial')),
                ('payment_day', models.PositiveIntegerField(verbose_name='Día de Pago')),
                ('discount', models.FloatField(default=0, verbose_name='Descuento')),
                ('balance', models.FloatField(blank=True, null=True, verbose_name='Saldo pendiente')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.cohort', verbose_name='Cohorte')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Matrícula',
                'verbose_name_plural': 'Matrículas',
                'unique_together': {('student', 'cohort')},
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('amount', models.FloatField()),
                ('payment_date', models.DateField()),
                ('status', models.BooleanField(choices=[(True, 'PAGADO'), (False, 'NO PAGADO')], default=False, verbose_name='Pagado')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments_enrollment', to='enrollment.enrollment')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
    ]
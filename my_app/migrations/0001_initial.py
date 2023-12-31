# Generated by Django 4.2.5 on 2023-10-01 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField()),
                ('loan_amount', models.IntegerField()),
                ('issued_by', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=24)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=28)),
                ('contact', models.CharField(max_length=15)),
                ('savings_balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saving_date', models.DateField()),
                ('saving_year', models.DateField(auto_now=True)),
                ('saving_month', models.DateField(auto_now=True)),
                ('amount', models.IntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='Loan_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('amount_paid', models.IntegerField()),
                ('received_by', models.CharField(max_length=24)),
                ('Loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.loan')),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.member'),
        ),
    ]

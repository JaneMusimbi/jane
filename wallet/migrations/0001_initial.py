# Generated by Django 4.1 on 2022-08-25 05:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField(null=True)),
                ('account_type', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('balance', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15, null=True)),
                ('lastname', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('phonenumber', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, null=True)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiptdate', models.DateTimeField()),
                ('file', models.FileField(max_length=15, upload_to='')),
                ('receipttype', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('currency', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=6, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.IntegerField()),
                ('pin', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=8, null=True)),
                ('transaction_amount', models.IntegerField(null=True)),
                ('transaction_type', models.CharField(max_length=38, null=True)),
                ('transaction_charge', models.IntegerField(null=True)),
                ('transaction_date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('destination_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_b', to='wallet.account')),
                ('origin_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_a', to='wallet.account')),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Thirdparty',
            fields=[
                ('name', models.CharField(max_length=15, null=True)),
                ('phone_number', models.CharField(max_length=105, null=True)),
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('points', models.IntegerField(null=True)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_number', models.IntegerField(null=True)),
                ('loan_type', models.CharField(max_length=32, null=True)),
                ('amount', models.BigIntegerField(null=True)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('loanbalance', models.IntegerField(null=True)),
                ('loanterm', models.IntegerField(null=True)),
                ('payduedate', models.DateTimeField(default=datetime.datetime.now)),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=15, null=True)),
                ('date_issue', models.DateTimeField(default=datetime.datetime.now)),
                ('card_type', models.CharField(max_length=14, null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
    ]

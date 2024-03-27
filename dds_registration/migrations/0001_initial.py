# Generated by Django 5.0.3 on 2024-03-27 19:44

import dds_registration.core.helpers.dates
import dds_registration.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(default=dds_registration.models.random_code, unique=True)),
                ('title', models.TextField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('public', models.BooleanField(default=False)),
                ('registration_open', models.DateField(auto_now_add=True, help_text='Date registration opens (inclusive)')),
                ('registration_close', models.DateField(help_text='Date registration closes (inclusive)')),
                ('max_participants', models.PositiveIntegerField(default=0, help_text='Maximum number of participants to this event (0 = no limit)')),
                ('currency', models.TextField(blank=True, null=True)),
                ('payment_deadline_days', models.IntegerField(default=30)),
                ('payment_details', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_no', models.IntegerField(primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.TextField(choices=[('CREATED', 'Created'), ('ISSUED', 'Issued'), ('PAID', 'Paid'), ('REFUNDED', 'Refunded')])),
                ('data', models.JSONField()),
                ('template', models.TextField(choices=[('M-CHF', 'Membership - Swiss Francs'), ('M-EUR', 'Membership - Euros'), ('G-USD', 'Generic - USD'), ('G-CHF', 'Generic - CHF'), ('G-EUR', 'Generic - EUR'), ('G-CAD', 'Generic - CAD')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(blank=True, default='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.IntegerField(default=dds_registration.core.helpers.dates.this_year)),
                ('until', models.IntegerField(default=dds_registration.core.helpers.dates.this_year)),
                ('honorary', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('membership_type', models.TextField(choices=[('NORMAL_CREDIT_CARD', 'Normal membership - Pay by credit card'), ('NORMAL_INVOICE', 'Normal membership - Pay by invoice'), ('ACADEMIC_CREDIT_CARD', 'Academic membership - Pay by credit card'), ('ACADEMIC_INVOICE', 'Academic membership - Pay by invoice')], default='NORMAL_CREDIT_CARD')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('emailed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dds_registration.event')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('currency', models.TextField(choices=[('USD', 'US Dollar'), ('CHF', 'Swiss Franc'), ('EUR', 'Euro'), ('CAD', 'Canadian Dollar')])),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dds_registration.event')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('status', models.TextField(choices=[('SUBMITTED', 'Application submitted'), ('SELECTED', 'Applicant selected'), ('WAITLIST', 'Applicant wait listed'), ('DECLINED', 'Applicant declined'), ('PAYMENT-PENDING', 'Registered (payment pending)'), ('REGISTERED', 'Registered'), ('WITHDRAWN', 'Withdrawn')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='dds_registration.event')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='dds_registration.invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to=settings.AUTH_USER_MODEL)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='dds_registration.registrationoption')),
            ],
        ),
        migrations.AddConstraint(
            model_name='registration',
            constraint=models.UniqueConstraint(condition=models.Q(('active', True)), fields=('event', 'user'), name='Single registration per verified user account'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-16 11:08

import accounts.managers
import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_no', models.CharField(blank=True, default='+', max_length=30, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Manage Account',
                'verbose_name_plural': 'Manage Accounts',
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Userpassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=256)),
                ('postal_code', models.CharField(blank=True, default=0, max_length=30, null=True)),
                ('country', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Client Address',
                'verbose_name_plural': 'Manage Client Address',
            },
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_id', models.IntegerField(choices=[(1, 'Starter Plan'), (2, 'Standard Plan'), (3, 'Platinum Plan'), (4, 'Gold Plan')])),
                ('invest_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('wallet', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.PositiveIntegerField(unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('wallet', models.DecimalField(decimal_places=2, default=5, max_digits=12)),
                ('direct_gateway', models.DecimalField(decimal_places=2, default=5, max_digits=12)),
                ('bitcoin', models.CharField(default='bc1qag2dva7c5wznevqlkt48pefs6dsjpg3gedurw3', max_length=120)),
                ('ethereum', models.CharField(default='0xc2a71F379d43206Ca47b2d5668D40ffA241160DC', max_length=120)),
                ('usdt_trc20', models.CharField(default='TCEjw4fDYdL2EfsQ5NhpuLxoJW9REkG8P8', max_length=120)),
                ('usdt_erc20', models.CharField(default='0xc2a71F379d43206Ca47b2d5668D40ffA241160DC', max_length=120)),
                ('total_profit', models.DecimalField(decimal_places=2, default=5, max_digits=12)),
                ('bonus', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('referral_bonus', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_deposit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_ticket', models.CharField(default=0, max_length=20)),
                ('total_investment', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('investment_bonus', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('signup_bonus', models.DecimalField(decimal_places=2, default=5, max_digits=12)),
                ('total_withdrawal', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_refferal', models.CharField(default=0, max_length=20)),
                ('picture', cloudinary.models.CloudinaryField(default='https://moonvillageassociation.org/wp-content/uploads/2018/06/default-profile-picture1-768x768.jpg', max_length=255, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fund Users Account',
                'verbose_name_plural': 'Fund Users Accounts',
            },
        ),
    ]

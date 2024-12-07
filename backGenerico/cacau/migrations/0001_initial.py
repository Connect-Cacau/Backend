# Generated by Django 5.1.4 on 2024-12-07 23:07

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
            name='Cacau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('cacauCategory', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('CHOCOLATE', 'Chocolate'), ('REGIONAL', 'Regional'), ('SERVICOS', 'Serviços'), ('COOPERATIVA', 'Cooperativa')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='empresas/')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=45)),
                ('estado', models.CharField(max_length=45)),
                ('latitude', models.IntegerField(blank=True, default=404)),
                ('longitude', models.IntegerField(blank=True, default=404)),
                ('cep', models.CharField(max_length=9)),
                ('logradouro', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoCacau', models.CharField(max_length=45)),
                ('mtdSecagem', models.CharField(max_length=45)),
                ('armazenamento', models.CharField(max_length=45)),
                ('tempoEstoque', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Producao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arroba', models.CharField(max_length=45)),
                ('ano', models.CharField(max_length=45)),
                ('trimestre', models.CharField(max_length=45)),
                ('sistemaProd', models.CharField(max_length=45)),
                ('variedadeCultivada', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('estadoCivil', models.CharField(max_length=9)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fermentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias', models.CharField(max_length=45)),
                ('loteFerm', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cacau.lote')),
            ],
        ),
        migrations.AddField(
            model_name='lote',
            name='loteProd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cacau.producao'),
        ),
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assisTec', models.CharField(max_length=45)),
                ('entidadeAssoc', models.CharField(max_length=45)),
                ('cadastroProd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cacau.cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Comercializacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoVenda', models.CharField(max_length=45)),
                ('tipoProd', models.CharField(max_length=45)),
                ('prodCom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cacau.produtor')),
            ],
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('arTotal', models.CharField(max_length=45)),
                ('arPreserv', models.CharField(max_length=45)),
                ('arCultivadaCacau', models.CharField(max_length=45)),
                ('arCultivaVeget', models.CharField(max_length=45)),
                ('areaRecuperada', models.CharField(max_length=45)),
                ('internet', models.PositiveSmallIntegerField()),
                ('desmatamento', models.PositiveSmallIntegerField()),
                ('degradacao', models.PositiveSmallIntegerField()),
                ('endProp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cacau.endereco')),
            ],
        ),
        migrations.AddField(
            model_name='producao',
            name='propProducao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cacau.propriedade'),
        ),
    ]

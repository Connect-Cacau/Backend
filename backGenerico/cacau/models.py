from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Cadastro(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome = models.CharField(max_length=45)
    estadoCivil = models.CharField(max_length=9)
    
    def __str__(self):
        return f"{self.nome}, {self.user.email}"

class Cacau(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250, blank=True, default='')
    cacauCategory = models.CharField(max_length=200, blank=False, default='')


class Endereco(models.Model):  
    municipio = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)
    latitude = models.IntegerField(blank=True, default=404)
    longitude = models.IntegerField(blank=True, default=404)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=90)
    
    def __str__(self):
        return f"{self.logradouro}, {self.cep} - {self.municipio}/{self.estado}"

class Produtor(models.Model):  
    assisTec = models.CharField(max_length=45)
    entidadeAssoc = models.CharField(max_length=45)
    cadastroProd = models.ForeignKey('Cadastro', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.assisTec}, {self.entidadeAssoc}, fk:{self.cadastroProd}"


class Comercializacao(models.Model):  
    tipoVenda = models.CharField(max_length=45)
    tipoProd = models.CharField(max_length=45)
    prodCom = models.ForeignKey('Produtor', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.tipoProd}, {self.tipoVenda}, fk:{self.prodCom}"


class Propriedade(models.Model):  
    nome = models.CharField(max_length=45)
    arTotal = models.CharField(max_length=45)
    arPreserv = models.CharField(max_length=45)
    arCultivadaCacau = models.CharField(max_length=45)
    arCultivaVeget = models.CharField(max_length=45)
    areaRecuperada = models.CharField(max_length=45)
    internet = models.PositiveSmallIntegerField()
    desmatamento = models.PositiveSmallIntegerField()
    degradacao = models.PositiveSmallIntegerField()
    endProp = models.ForeignKey('Endereco', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}, {self.desmatamento}, fk:{self.endProp}"


class Producao(models.Model):  
    arroba = models.CharField(max_length=45)  
    ano = models.CharField(max_length=45)  
    trimestre = models.CharField(max_length=45)  
    sistemaProd = models.CharField(max_length=45) 
    variedadeCultivada = models.CharField(max_length=45)  
    propProducao = models.ForeignKey('Propriedade', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.arroba}, {self.ano}, fk:{self.propProducao}"


class Lote(models.Model):  
    tipoCacau = models.CharField(max_length=45)  
    mtdSecagem = models.CharField(max_length=45)  
    armazenamento = models.CharField(max_length=45)  
    tempoEstoque = models.CharField(max_length=45)  
    loteProd = models.ForeignKey('Producao', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.tipoCacau}, {self.mtdSecagem}, fk:{self.loteProd}"


class Fermentacao(models.Model):  
    dias = models.CharField(max_length=45)  
    loteFerm = models.ForeignKey('Lote', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.dias}, {self.loteFerm}, fk:{self.loteFerm}"


class Empresa(models.Model):
    TIPO_CHOICES = (
        ('CHOCOLATE', 'Chocolate'),
        ('REGIONAL', 'Regional'),
        ('SERVICOS', 'Serviços'),
        ('COOPERATIVA', 'Cooperativa'),
    )
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    image = models.ImageField(upload_to='empresas/', null=True, blank=True)
    
    def __str__(self):
        return self.nome
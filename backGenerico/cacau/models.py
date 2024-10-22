from django.db import models


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


class Cadastro(models.Model):  
    nome = models.CharField(max_length=45)
    estadoCivil = models.CharField(max_length=9)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nome}, {self.email}"


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

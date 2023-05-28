from django.db import models
from datetime import date
# Create  your models here


class Produit(models.Model):
    Type_CHOICES = [('fr', 'Frais'), ('cs', 'Conserve'), ('em', 'emballé')]
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Nom définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    imag = models.ImageField(blank=True)
    type = models.CharField(max_length=2, choices=Type_CHOICES, default='em')
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    Fournisseur = models.ForeignKey('Fournisseur', on_delete=models.CASCADE,null=True) 
    def __str__(self):
        return self.libelle+" "+self.description+" "+str(self.prix)+" "


class Categorie(models.Model):
    Type_CHOICES = [('AI', 'Alimentair'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'),
                    ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor')]
    name = models.CharField(max_length=50, default='Alimentair',choices=Type_CHOICES)
    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adress= models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom+" "+self.adress+" "+self.email+" "+self.telephone
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return super().__str__()+" "+self.Duree_garantie
class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
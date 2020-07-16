from django.db import models
import datetime

class Item(models.Model):
        titolo = models.CharField(max_length=100, blank=True, default='')
        modello = models.CharField(max_length=100, blank=True, default='')
        prezzo = models.CharField(max_length=50, blank=True, default='')
        immagine_principale = models.ImageField(blank=True, default='')
        url = models.URLField(blank=True)
        marca = models.CharField(max_length=100, blank=True, default='')
        anno = models.CharField(max_length=100, blank=True, default='')
        chilometraggio = models.CharField(max_length=100, blank=True, default='')
        motore = models.CharField(max_length=100, blank=True, default='')
        carburante = models.CharField(max_length=100, blank=True, default='')
        cambio = models.CharField(max_length=100, blank=True, default='')
        classe = models.CharField(max_length=100, blank=True, default='')
        colore = models.CharField(max_length=100, blank=True, default='')
        lunghezza = models.CharField(max_length=100, blank=True, default='')
        larghezza = models.CharField(max_length=100, blank=True, default='')
        altezza = models.CharField(max_length=100, blank=True, default='')
        posti_letto = models.CharField(max_length=100, blank=True, default='')
        posti_omologati = models.CharField(max_length=100, blank=True, default='')
        peso_a_pieno_carico = models.CharField(max_length=100, blank=True, default='')
        descrizione = models.CharField(max_length=2000, blank=True, default='')
        immagine_02 = models.ImageField(blank=True, default='')
        immagine_03 = models.ImageField(blank=True, default='')
        immagine_04 = models.ImageField(blank=True, default='')
        immagine_05 = models.ImageField(blank=True, default='')
        immagine_06 = models.ImageField(blank=True, default='')
        immagine_07 = models.ImageField(blank=True, default='')
        immagine_08 = models.ImageField(blank=True, default='')
        immagine_09 = models.ImageField(blank=True, default='')
        immagine_10 = models.ImageField(blank=True, default='')
        immagine_11 = models.ImageField(blank=True, default='')
        immagine_12 = models.ImageField(blank=True, default='')
        immagine_13 = models.ImageField(blank=True, default='')
        immagine_14 = models.ImageField(blank=True, default='')
        immagine_15 = models.ImageField(blank=True, default='')
        immagine_16 = models.ImageField(blank=True, default='')

        data_inserzione = models.DateField(default=datetime.date.today)

        def __str__(self):
            return self.titolo

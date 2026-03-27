from django.db import models

TYPE_CHOICES = [
    ('korneplod', 'Корнеплод'),
    ('klubneplod', 'Клубнеплоды'),
    ('kapystnye', 'Капустные'),
    ('paslenovy', 'Паслёновые'),
    ('lukony', 'Луковые'),
    ('tykvenny', 'Тыквенные'),
    ('zelensky', 'Зелень'),
]

class Product(models.Model):
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"({self.type}) {self.name} {self.price}с/кг"
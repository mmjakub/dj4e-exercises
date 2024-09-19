from django.core.validators import MinLengthValidator
from django.db.models import Model, CharField, PositiveIntegerField, ForeignKey, CASCADE

class Breed(Model):
    name = CharField(
            max_length=200,
            validators=[MinLengthValidator(2, 'Breed must be greater than 1 character')]
            )
    
    def __str__(self):
        return self.name

class Cat(Model):
    nickname = CharField(
            max_length=200,
            validators=[MinLengthValidator(2, 'Nickname must be greater than 1 character')]
            )
    weight = PositiveIntegerField()
    foods = CharField(max_length=300)
    breed = ForeignKey('Breed', on_delete=CASCADE, null=False)
    
    def __str__(self):
        return self.nickname

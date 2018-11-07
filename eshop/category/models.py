from django.db import models

# Create your models here.

CHOICE_CATEGORY  = (
    ('laptops' , 'Ноутбуки'),
    ('mobile_phones' , 'Телефоны'),
    ('tablet' , 'Планшеты'),
    ('source_details' , 'Комплектующие'),
    ('nau' , 'Наушники')
)



class Category(models.Model):
    name = models.CharField(max_length=100 ,  verbose_name= 'Категория'  , choices=CHOICE_CATEGORY)

    def __str__(self):
        return self.name


OPERATION_SYSTEM = (
    ('mac' , 'MacOS'),
    ('linux' , 'Linux'),
    ('windows' , 'Windows')
)

TYPE_MONITOR  = (
    ('glossy'  , 'Глянцевый'),
    ('matt'  , 'Матовый')
)

class Laptop(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    model =  models.CharField(max_length=255 , verbose_name='Модель ноутбука' , default='i534')
    brand =  models.CharField(max_length=255 , verbose_name='Бренд ' , default='Apple')
    diagonal =  models.CharField(max_length=255 , verbose_name='Диагональ ' , default='12')
    oper_system =  models.CharField(max_length=255 , verbose_name='Операционная система' , choices=OPERATION_SYSTEM)
    oper_memory = models.IntegerField(verbose_name='ОЗУ' , default=16)
    type_monitor = models.CharField(max_length=255 , verbose_name='Тип экрана' , choices=TYPE_MONITOR)
    count_core = models.IntegerField(verbose_name='Количество ядер' , default=8)
    price = models.IntegerField(verbose_name='Цена' , default='50000')
    image = models.ImageField(upload_to='images/', blank=True, null=True ,  verbose_name='Картинка')

    def __str__(self):
        return 'Модель - {} Бренд - {}'.format(self.model , self.brand)

    def get_all(self):
        return Laptop.objects.all()

    def delete_all(self):
        return Laptop.objects.all().delete()
from django.db import models


class Seller(models.Model):
    """
    Модель, представляющая продавца электроники

    Поля:
    - title (CharField): Название продавца
    - email (EmailField): Email
    - country (CharField): Страна
    - city (CharField): Город
    - street (CharField): Улица
    - number_home (IntegerField): Номер дома
    - product (ForeignKey): Товар, продаваемый продавцом
    - provider (ForeignKey): Поставщик
    - level (CharField): Уровень в иерархии ( '0', '1', '2')
    - debt (DecimalField): задолженность перед поставщиком
    - create_date (DateField): Дата создания продавца в БД
    """

    class Level(models.IntegerChoices):
        FACTORY = 0, 'Завод'
        RETAILER = 1, 'Розничная сеть'
        IP = 2, 'Индивидуальный предприниматель'

    title = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    number_home = models.IntegerField(verbose_name='номер дома')
    product = models.ManyToManyField('Product', verbose_name='товар')
    provider = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='поставщик')
    level = models.IntegerField(choices=Level.choices, verbose_name='уровень')
    debt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='задолженность')
    create_date = models.DateField(auto_now_add=True, verbose_name='дата добавления')

    def __str__(self):
        return f'{self.title}, {self.country},{self.city}'

    class Meta:
        verbose_name = 'продавец'
        verbose_name_plural = 'продавцы'


class Product(models.Model):
    """
    Модель товара
    Поля:
    - title (CharField): Название товара
    - product_model (CharField): модель товара
    -  launch_date(DateField): дата выхода товара на рынок
    """
    
    title = models.CharField(max_length=255, verbose_name='товар')
    product_model = models.CharField(max_length=255, verbose_name='модель')
    launch_date = models.DateField(verbose_name='дата выхода товара на рынок')

    def __str__(self):
        return f'{self.title} {self.product_model}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

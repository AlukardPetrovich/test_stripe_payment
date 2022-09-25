from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.TextField(verbose_name='Назвние товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.IntegerField(verbose_name='Стоимость товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'


class OrderedItem(models.Model):
    item = models.ForeignKey(
        Item,
        verbose_name=('Товар'),
        on_delete=models.PROTECT
    )
    amount = models.IntegerField(
        verbose_name='Количество товаров в заказе',
        default=0,
        validators=[MinValueValidator(0)]
    )
    order = models.ForeignKey(
        'Order',
        verbose_name='Заказ',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказах'

    def __str__(self):
        return (f'{self.amount} шт. товара {self.item}'
                ' добавлено в заказ {self.order}')


class Order(models.Model):
    item = models.ManyToManyField(
        Item,
        verbose_name='Товар',
        through=OrderedItem
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ № {self.id}'

# from django.db import models

# # Create your models here.

# MAX_LENGTH = 255

# class Order(models.Model):
#     SHOP = "SH"
#     COURIER = "CR"
#     PICKUPPOINT = "PP"
    
#     TYPE_DELIVERY = [
#         (SHOP, 'Вывоз из магазина'),
#         (COURIER, 'Курьер'),
#         (PICKUPPOINT, 'Пункт выдачи заказов'),
#     ]

#     buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия покупателя')
#     buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя покупателя')
#     buyer_surname = models.CharField(
#         max_length=MAX_LENGTH, 
#         blank=True, 
#         null=True,
#         verbose_name='Отчество покупателя'
#     )
#     comment = models.CharField(
#         max_length=MAX_LENGTH, 
#         blank=True, 
#         null=True, 
#         verbose_name='Комментарий к заказу'
#     )
#     delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
#     delivery_type = models.CharField(
#         max_length=2, 
#         choices=TYPE_DELIVERY, 
#         default=SHOP, 
#         verbose_name='Способ доставки'
#     )
#     date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
#     date_finish = models.DateTimeField(
#         null=True, 
#         blank=True, 
#         verbose_name='Дата завершения заказа'
#     )
#     clothes = models.ManyToManyField('Clothes', through='Pos_order', verbose_name='Товар')

#     def __str__(self):
#         return f'#{self.pk} - {self.buyer_firstname} {self.buyer_name} ({self.date_create})'

#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'


# class Pos_order(models.Model):
#     clothes = models.ForeignKey(
#         Teacher, 
#         on_delete=models.PROTECT, 
#         verbose_name='Продукт'
#     )
#     order = models.ForeignKey(
#         Order, 
#         on_delete=models.PROTECT, 
#         verbose_name='Заказ'
#     )
#     count = models.PositiveIntegerField(default=1, verbose_name='Количество продукта')
#     discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на позицию')

#     def __str__(self):
#         return f'{self.order.pk} {self.clothes.name} ({self.order.buyer_firstname} {self.order.buyer_name})'

#     class Meta:
#         verbose_name = 'Позиция заказа'
#         verbose_name_plural = 'Позиции заказов'
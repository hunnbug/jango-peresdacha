from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

MAX_LENGTH_SHORT = 50
MAX_LENGTH_MEDIUM = 100
MAX_LENGTH_LONG = 255
MAX_LENGTH_ID = 20
MAX_LENGTH_PHONE = 11
MAX_LENGTH_CODE = 10
MAX_LENGTH_ROOM = 4
MAX_LENGTH_LETTER = 1
MAX_LENGTH = 255


class Subject(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_MEDIUM)

    class Meta:
        verbose_name='Предмет'
        verbose_name_plural='Предметы'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    # teacher_id = models.CharField(max_length=MAX_LENGTH_ID, unique=True)
    first_name = models.CharField(max_length=MAX_LENGTH_SHORT)
    surname = models.CharField(max_length=MAX_LENGTH_SHORT)
    last_name = models.CharField(max_length=MAX_LENGTH_SHORT)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=MAX_LENGTH_PHONE, blank=True)
    email = models.EmailField(blank=True)
    subject = models.ForeignKey(Subject, related_name='teachers', on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(999999)], default=1)

    class Meta:
        verbose_name='Учитель'
        verbose_name_plural='Учителя'

    def __str__(self):
        return f"{self.surname} {self.first_name} {self.last_name}"


class Class_group(models.Model):
    
    CLASS_LEVELS = [
        ('1', '1 класс'),
        ('2', '2 класс'),
        ('3', '3 класс'),
        ('4', '4 класс'),
        ('5', '5 класс'),
        ('6', '6 класс'),
        ('7', '7 класс'),
        ('8', '8 класс'),
        ('9', '9 класс'),
        ('10', '10 класс'),
        ('11', '11 класс'),
    ]
    
    letter = models.CharField(max_length=MAX_LENGTH_LETTER)
    grade = models.CharField(max_length=2, choices=CLASS_LEVELS)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='classes')
    room_number = models.CharField(max_length=MAX_LENGTH_ROOM, null=True)

    class Meta:
        verbose_name='Класс'
        verbose_name_plural='Классы'

    def __str__(self):
        return f"{self.grade}{self.letter}"


class Student(models.Model):
    student_id = models.CharField(max_length=MAX_LENGTH_ID, unique=True)
    first_name = models.CharField(max_length=MAX_LENGTH_SHORT)
    surname = models.CharField(max_length=MAX_LENGTH_SHORT)
    last_name = models.CharField(max_length=MAX_LENGTH_SHORT)
    date_of_birth = models.DateField()
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=MAX_LENGTH_PHONE, blank=True)
    parent_name = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True)
    parent_middlename = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True)
    parent_phone = models.CharField(max_length=MAX_LENGTH_PHONE, blank=True)
    class_group = models.ForeignKey(Class_group, related_name="student", on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(upload_to='studуnts/', null=True, blank=True)

    class Meta:
        verbose_name='Ученик'
        verbose_name_plural='Ученики'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('MON', 'Понедельник'),
        ('TUE', 'Вторник'),
        ('WED', 'Среда'),
        ('THU', 'Четверг'),
        ('FRI', 'Пятница'),
        ('SAT', 'Суббота'),
    ]
    
    class_group = models.ForeignKey(Class_group, on_delete=models.CASCADE, related_name='schedules')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=MAX_LENGTH_ROOM)

    class Meta:
        verbose_name='Расписание'
        verbose_name_plural='Расписания'

    def __str__(self):
        return f"{self.day_of_week} {self.teacher} {self.subject}"



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_given = models.DateField(auto_now_add=True)
    semester = models.IntegerField(choices=[(1, '1 семестр'), (2, '2 семестр')])

    class Meta:
        verbose_name='Оценка'
        verbose_name_plural='Оценки'

    def __str__(self):
        return f"{self.student} {self.subject} {self.grade}"

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Присутствовал'),
        ('N', 'Отсутствовал'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    class Meta:
        verbose_name='Посещаемость'
        verbose_name_plural='Посещаемости'

    def __str__(self):
        return f"{self.student} {self.schedule} {self.status}"


class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class_group, on_delete=models.CASCADE, related_name='homeworks')
    description = models.TextField()
    assigned_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    class Meta:
        verbose_name='Домашнее задание'
        verbose_name_plural='Домашние задания'

    def __str__(self):
        return f"{self.subject} {self.due_date} {self.description}"


class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    
    TYPE_DELIVERY = [
        (SHOP, 'Вывоз из магазина'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ]

    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия покупателя')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя покупателя')
    buyer_surname = models.CharField(
        max_length=MAX_LENGTH, 
        blank=True, 
        null=True,
        verbose_name='Отчество покупателя'
    )
    comment = models.CharField(
        max_length=MAX_LENGTH, 
        blank=True, 
        null=True, 
        verbose_name='Комментарий к заказу'
    )
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(
        max_length=2, 
        choices=TYPE_DELIVERY, 
        default=SHOP, 
        verbose_name='Способ доставки'
    )
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(
        null=True, 
        blank=True, 
        verbose_name='Дата завершения заказа'
    )
    teachers = models.ManyToManyField('Teacher', through='Pos_order', verbose_name='Товар')
    price = models.DecimalField(max_digits=9, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(999999999)], default=1)

    def __str__(self):
        return f'#{self.pk} - {self.buyer_firstname} {self.buyer_name} ({self.date_create})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Pos_order(models.Model):
    teacher = models.ForeignKey(
        Teacher, 
        on_delete=models.PROTECT, 
        verbose_name='Продукт'
    )
    order = models.ForeignKey(
        Order, 
        on_delete=models.PROTECT, 
        verbose_name='Заказ'
    )
    count = models.PositiveIntegerField(default=1, verbose_name='Количество продукта')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на позицию')

    def __str__(self):
        return f'{self.order.pk} {self.teacher} ({self.order.buyer_firstname} {self.order.buyer_name})'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
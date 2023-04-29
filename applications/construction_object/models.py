from django.db import models
from django.utils.translation import gettext_lazy as _


class SideChoices(models.TextChoices):
    north = ('Север', _('Север'))
    south = ('Юг', _('Юг'))
    east = ('Восток', _('Восток'))
    west = ('Запад', _('Запад'))


class District(models.Model):
    title = models.CharField(verbose_name='название', max_length=256, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class OfferChoice(models.TextChoices):
    start_sale = ('Старт продаж', _('Старт продаж'))
    ten_percent = ('Скидки до 10%', _('Скидки до 10%'))
    last_sale = ('Последнее предложение', _('Последнее предложение'))
    sales_complete = ('Продажи завершины', _('Продажи завершины'))


class ConstructionStateChoice(models.TextChoices):
    ten = ('10%', '10%')
    twenty = ('20%', '20%')
    thirty = ('30%', '30%')
    fourty = ('40%', '40%')
    fifty = ('50%', '50%')
    sixty = ('60%', '60%')
    seventy = ('70%', '70%')
    eighty = ('80%', '80%')
    ninety = ('90%', '90%')
    hundred = ('100%', '100%')


class Quarter(models.TextChoices):
    first = ('I', _('Сдача в I квартале'))
    second = ('II', _('Сдача в II квартале'))
    third = ('III', _('Сдача в III квартале'))
    fourth = ('IV', _('Сдача в IV квартале'))


class Year(models.Model):
    year = models.CharField(verbose_name='год', max_length=256, unique=True)

    def __str__(self):
        return f'{self.year}'

    class Meta:
        verbose_name = 'Год сдачи объекта'
        verbose_name_plural = 'Года сдачи объектов'


class ConstructionTypeChoice(models.TextChoices):
    residential = ('жилой', _('Жилой'))
    commercial = ('коммерческий', _('Коммерческий'))


class Construction(models.Model):
    type = models.CharField(verbose_name='тип объекта', max_length=256, choices=ConstructionTypeChoice.choices,
                            blank=True, null=True)
    title = models.CharField(verbose_name='название', max_length=256, unique=True)
    main_picture = models.ImageField(verbose_name='Главная фотография', upload_to='construction_images')
    street_address = models.CharField(verbose_name='адрес улицы', max_length=200)
    district = models.ForeignKey(District, verbose_name='район', related_name='construction_district',
                                 on_delete=models.DO_NOTHING, blank=True, null=True)
    latitude = models.DecimalField(verbose_name='широта', max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(verbose_name='долгота', max_digits=9, decimal_places=6, blank=True, null=True)
    offer = models.CharField(verbose_name="предложение", max_length=256, choices=OfferChoice.choices,
                             blank=True, null=True)
    cost_per_square_meter = models.DecimalField(verbose_name='Стоимость за 1 m2', max_digits=10, decimal_places=2)
    construction_state = models.CharField(verbose_name='готовность объекта', max_length=256,
                                          choices=ConstructionStateChoice.choices, default='10%', blank=True, null=True)
    construction_completion_quarter = models.CharField(verbose_name='квартал сдачи объекта', max_length=256,
                                          choices=Quarter.choices, default='1 квартал', blank=True, null=True)
    construction_completion_year = models.ForeignKey(Year, verbose_name='год сдачи объекта',
                                                     related_name='construction_completion_year',
                                                     on_delete=models.DO_NOTHING, blank=True, null=True)
    min_price = models.PositiveIntegerField(verbose_name='Минимальная цена от', blank=True, null=True)
    installment = models.CharField(verbose_name='в рассрочку', max_length=256, blank=True, null=True)
    description = models.TextField(verbose_name='описание объекта', blank=True, null=True)
    youtube_link = models.URLField(verbose_name='ссылка на видео', blank=True, null=True)
    is_selling = models.BooleanField(verbose_name='в продаже', default=False)
    is_completed = models.BooleanField(verbose_name='построен', default=False)
    key_words = models.CharField(verbose_name='Ключевые слова', max_length=556, blank=True, null=True)

    def __str__(self):
        return f'{self.title}, {self.street_address}'

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class ConstructionImage(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, related_name='construction_image')
    image = models.ImageField(verbose_name='Фотографии', upload_to='construction_images', blank=True, null=True)

    class Meta:
        verbose_name = 'Фотография объекта'
        verbose_name_plural = 'Фотографии объекта'


class Advantage(models.Model):
    construction = models.ManyToManyField(Construction, verbose_name='Объект',
                                          related_name='advantage_of_construction')
    description = models.TextField(verbose_name='краткое описание', blank=True, null=True)
    logo = models.ImageField(verbose_name='лого', upload_to='advantage_logo', blank=True, null=True)

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'Плюс объекта'
        verbose_name_plural = 'Плюсы объекта'


class Feature(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, verbose_name='объект',
                                     related_name='features', blank=True, null=True)
    title = models.CharField(verbose_name='название особенности', max_length=255, blank=True, null=True)
    description = models.TextField(verbose_name='описание особенности', blank=True, null=True)
    picture = models.ImageField(upload_to='features', verbose_name='фотография', blank=True, null=True)

    def __str__(self):
        return f'{self.construction.title}-{self.title}'

    class Meta:
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенности'


class Block(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, verbose_name='объект',
                                     related_name='block_objects', blank=True, null=True)
    block_name = models.CharField(verbose_name='Название', max_length=256)
    plan_model = models.FileField(verbose_name='План', blank=True, null=True)
    sides = models.CharField(verbose_name='Сторона', max_length=20, choices=SideChoices.choices, blank=True, null=True)
    is_sold = models.BooleanField(verbose_name='Продан', default=False)

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        return f'{self.construction.title} - {self.block_name}'


class RoomsCount(models.TextChoices):
    studio = ('Studio', 'Студия')
    one = ('1', _('1 комната'))
    two = ('2', _('2 комнаты'))
    three = ('3', _('3 комнаты'))
    four = ('4', _('4 комнаты'))
    five = ('5', _('5 комнат'))


class FlatTypeChoice(models.TextChoices):
    residential = ('жилой', _('Жилой'))
    commercial = ('коммерческий', _('Коммерческий'))


class Flat(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, verbose_name='объект',
                                     related_name='layout', blank=True, null=True)
    block = models.ForeignKey(Block, verbose_name='корпус', on_delete=models.CASCADE, related_name='block_flat',
                              blank=True, null=True)
    type = models.CharField(verbose_name='тип помещения', max_length=256, choices=FlatTypeChoice.choices,
                            blank=True, null=True)
    layout_photo = models.ImageField(verbose_name='планировка ', upload_to='layouts', blank=True, null=True)
    design_photo = models.ImageField(verbose_name='3D модель', upload_to='layouts/', blank=True, null=True)
    rooms = models.CharField(verbose_name='количество комнат', max_length=6, choices=RoomsCount.choices,
                             blank=True, null=True)
    square_meters = models.PositiveIntegerField(verbose_name='площадь помещения', blank=True, null=True)
    floor = models.IntegerField(verbose_name='этаж', blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена', blank=True, null=True)
    mortgage = models.CharField(verbose_name='в ипотеку', max_length=256, blank=True, null=True)

    def __str__(self):
        return f'{self.construction.title}-{self.type}-{self.square_meters}m2'

    class Meta:
        verbose_name = 'Планировка'
        verbose_name_plural = 'Планировки'


class Infrastructure(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, verbose_name='объект',
                                     related_name='infrasrtucture_nearby', blank=True, null=True)
    culture = models.PositiveIntegerField(verbose_name='Культура и отдых', blank=True, null=True)
    medicine = models.PositiveIntegerField(verbose_name='Медицина', blank=True, null=True)
    education = models.PositiveIntegerField(verbose_name='Образование', blank=True, null=True)
    finance = models.PositiveIntegerField(verbose_name='Финансы', blank=True, null=True)
    trade = models.PositiveIntegerField(verbose_name='Торговля', blank=True, null=True)
    food = models.PositiveIntegerField(verbose_name='Еда', blank=True, null=True)
    sport = models.PositiveIntegerField(verbose_name='Спорт', blank=True, null=True)
    service = models.PositiveIntegerField(verbose_name='Услуги', blank=True, null=True)

    def __str__(self):
        return f'{self.construction}'

    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Инфраструктуры'

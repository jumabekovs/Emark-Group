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
    new = ('новый', _('новый'))
    on_process = ('в процессе', _('в процессе'))
    end_process = ('в завершении', _('в завершении'))


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


class SellingStatus(models.TextChoices):
    selling = ('selling', _('в продаже'))
    built = ('built', _('построено'))


class ClassObj(models.TextChoices):
    economy = ('эконом', _('эконом'))
    comfort = ('комфорт', _('комфорт'))
    business = ('бизнес', _('бизнес'))
    premium = ('премиум', _('премиум'))


class Construction(models.Model):
    type = models.CharField(verbose_name='тип объекта', max_length=256, choices=ConstructionTypeChoice.choices,
                            blank=True, null=True)
    class_obj = models.CharField(max_length=25, choices=ClassObj.choices, verbose_name='класс', blank=True, null=True)
    selling_status = models.CharField(max_length=25, choices=SellingStatus.choices,
                                      verbose_name='статус', default='в продаже')
    offer = models.CharField(verbose_name="предложение", max_length=256, choices=OfferChoice.choices,
                             blank=True, null=True)
    key_words = models.CharField(verbose_name='ключевые слова (SEO)', max_length=556, blank=True, null=True)
    title = models.CharField(verbose_name='название', max_length=256, unique=True)
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='construction_images')
    street_address = models.CharField(verbose_name='адрес улицы', max_length=200)
    district = models.ForeignKey(District, verbose_name='район', related_name='construction_district',
                                 on_delete=models.DO_NOTHING, blank=True, null=True)
    latitude = models.DecimalField(verbose_name='широта', max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(verbose_name='долгота', max_digits=9, decimal_places=6, blank=True, null=True)
    cost_per_square_meter = models.DecimalField(verbose_name='стоимость за 1 m2', max_digits=10, decimal_places=2)
    construction_state = models.CharField(verbose_name='готовность объекта', max_length=256,
                                          choices=ConstructionStateChoice.choices, default='10%', blank=True, null=True)
    construction_completion_quarter = models.CharField(verbose_name='квартал сдачи объекта', max_length=256,
                                          choices=Quarter.choices, default='1 квартал', blank=True, null=True)
    construction_starting_year = models.DateField(verbose_name='год начала строительства', blank=True, null=True)
    construction_completion_year = models.ForeignKey(Year, verbose_name='год сдачи объекта',
                                                     related_name='construction_completion_year',
                                                     on_delete=models.DO_NOTHING, blank=True, null=True)
    min_price = models.PositiveIntegerField(verbose_name='минимальная цена от', blank=True, null=True)
    installment = models.CharField(verbose_name='в рассрочку', max_length=256, blank=True, null=True)
    description = models.TextField(verbose_name='описание объекта', blank=True, null=True)
    youtube_link = models.URLField(verbose_name='ссылка на видео', blank=True, null=True)

    def __str__(self):
        return f'{self.title}, {self.street_address}'

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class ConstructionImage(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, related_name='construction_image')
    image = models.ImageField(verbose_name='фотографии', upload_to='construction_images', blank=True, null=True)

    class Meta:
        verbose_name = 'Фотография объекта'
        verbose_name_plural = 'Фотографии объекта'


class Advantage(models.Model):
    construction = models.ManyToManyField(Construction, verbose_name='объект',
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
    block_name = models.CharField(verbose_name='название', max_length=256)
    plan_model = models.FileField(verbose_name='план', blank=True, null=True)
    sides = models.CharField(verbose_name='сторона', max_length=20, choices=SideChoices.choices, blank=True, null=True)
    is_sold = models.BooleanField(verbose_name='продан', default=False)

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
    rooms = models.CharField(verbose_name='количество комнат', max_length=6, choices=RoomsCount.choices,
                             blank=True, null=True)
    floor = models.IntegerField(verbose_name='этаж', blank=True, null=True)
    square_meters = models.PositiveIntegerField(verbose_name='площадь помещения', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена', blank=True, null=True)
    mortgage = models.CharField(verbose_name='в ипотеку', max_length=256, blank=True, null=True)

    def __str__(self):
        return f'{self.construction.title}-{self.type}-{self.square_meters}m2'

    class Meta:
        verbose_name = 'Планировка'
        verbose_name_plural = 'Планировки'


class Room(models.Model):
    flat = models.ForeignKey(Flat, related_name='room', on_delete=models.CASCADE)
    hall = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='холл', blank=True, null=True)
    dining_room = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='гостинная', blank=True, null=True)
    kitchen = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='кухня', blank=True, null=True)
    balcony_1 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='балкон 1', blank=True, null=True)
    balcony_2 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='балкон 2', blank=True, null=True)
    balcony_3 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='балкон 3', blank=True, null=True)
    bath = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='ванная', blank=True, null=True)
    wc_1 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='санузел 1', blank=True, null=True)
    wc_2 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='санузел 1', blank=True, null=True)
    bed_room_1 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='спальня 1', blank=True, null=True)
    bed_room_2 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='спальня 2', blank=True, null=True)
    bed_room_3 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='спальня 3', blank=True, null=True)

    class Meta:
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'


class FlatImages(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='flat_images', blank=True, null=True)
    image = models.ImageField(verbose_name='фото квартиры', blank=True, null=True)

    class Meta:
        verbose_name = 'Фото Объекта'
        verbose_name_plural = 'Фото Объектов'


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


class PriceList(models.Model):
    construction = models.ForeignKey(Construction, related_name='price_list',
                                     on_delete=models.CASCADE, verbose_name='объект', blank=True, null=True)
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2)
    date = models.DateField(verbose_name='дата', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='актуальный', default=False)

    def __str__(self):
        return f'{self.construction} - {self.date} - {self.price}'

    class Meta:
        verbose_name = 'Прайс Лист'
        verbose_name_plural = 'Прайс Лист'

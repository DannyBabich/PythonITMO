from django.core.exceptions import ValidationError
from django.test import TestCase

from gallerydept.models import Section, Product


class MyTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('setUpTestData - запущен')

    def setUp(self):
        print('setUp - запущен')

    def tearDown(self):
        print('tearDown - тест завершен')

    def test1(self):
        print('Запущен тест на криворукость')
        self.assertTrue(True)

    # def test2(self):
    #     print('Запущен тест на криворукость - 2')
    #     self.assertTrue(False)


    @classmethod
    def setUpTestData(cls):
        Section.objects.create(title='Main', slug='main') #перенос информации в резервную базу данных

    def test_title_max_length(self):
        obj = Section.objects.get(id=1)
        max_length = obj._meta.get_field('title').max_length
        self.assertEqual(max_length, 70)

    def test_title_help_text(self):
        obj = Section.objects.get(id=1)
        help_text = obj._meta.get_field('title').help_text
        self.assertEqual(help_text, 'Тут надо ввести название раздела')

    def test_title_unique(self):
        obj = Section.objects.get(id=1)
        unique = obj._meta.get_field('title').unique
        self.assertTrue(unique)

    def test_title_verbose_name(self):
        obj = Section.objects.get(id=1)
        verbose_name = obj._meta.get_field('title').verbose_name
        self.assertEqual(verbose_name, 'Название раздела')

    def test_slug_max_length(self):
        obj = Section.objects.get(id=1)
        max_length = obj._meta.get_field('slug').max_length
        self.assertEqual(max_length, 40)

    def test_slug_verbose_name(self):
        obj = Section.objects.get(id=1)
        verbose_name = obj._meta.get_field('slug').verbose_name
        self.assertEqual(verbose_name, 'Псевдоним')

    def test_slug_default(self):
        obj = Section.objects.get(id=1)
        default = obj._meta.get_field('slug').default
        self.assertEqual(default, '')

    def test_meta_ordering(self):
        obj = Section.objects.get(id=1)
        ordering = obj._meta.ordering
        self.assertEqual(ordering, ['id'])

    def test_meta_verbose_name(self):
        obj = Section.objects.get(id=1)
        verbose_name = obj._meta.verbose_name
        self.assertEqual(verbose_name, 'Раздел')

    def test_meta_verbose_name_plural(self):
        obj = Section.objects.get(id=1)
        verbose_name_plural = obj._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Разделы')

    def test_get_absolute_url(self):
        obj = Section.objects.get(id=1)
        self.assertEqual(obj.get_absolute_url(), '/gallerydept/section/' + obj.slug)

    @classmethod
    def setUpTestData(cls):
        Section.objects.create(title='Main', slug='main')
        Product.objects.create(
            title='Title', slug='title',
            section=Section.objects.get(id=1),
            price=200,
            year=2001,
            country='Россия',
            author='Художник',
            materials='Матерьялы',
            description='Описание'
        )

    def test_section_null(self):
        obj = Product.objects.get(id=1)
        self.assertTrue(obj._meta.get_field('section').null)

    def test_image_upload_to(self):
        obj = Product.objects.get(id=1)
        self.assertTrue(obj._meta.get_field('image').upload_to, 'images')

    def test_year(self):
        obj = Product.objects.get(id=1)
        obj.year = 1999
        self.assertRaises(ValidationError, obj.full_clean)
        obj.year = 2030
        self.assertRaises(ValidationError, obj.full_clean)

    def test_meta_ordering(self):
        obj = Product.objects.get(id=1)
        ordering = obj._meta.ordering
        self.assertEqual(ordering, ['title', '-price'])

    def test_count(self):
        obj = Product.objects.get(id=1)
        obj.count = 5
        self.assertEqual(obj.get_count(), 5)

    def test_get_sum_price(self):
        obj = Product.objects.get(id=1)
        obj.count = 2
        self.assertEqual(obj.get_sum_price(), 400)

    def test_str(self):
        obj = Product.objects.get(id=1)
        self.assertEqual(str(obj), 'Title (Main)')

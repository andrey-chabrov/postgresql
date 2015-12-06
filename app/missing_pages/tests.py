from django.test import TestCase
from django.db import connection

from . import models


class TestGetMissingPages(TestCase):

    fixtures = ('test_missing_pages.json',)

    def setUp(self):
        pass

    def test_versions_count_more_than_students_one_1(self):
        test_id = models.Test.objects.get(name='one-t').pk
        version_name = 'two-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = [('one-s', 'two-v', [2])]
        self.assertEquals(result, test)

    def test_versions_count_more_than_students_one_2(self):
        test_id = models.Test.objects.get(name='one-t').pk
        version_name = 'one-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = []
        self.assertEquals(result, test)

    def test_versions_count_more_than_students_one_3(self):
        test_id = models.Test.objects.get(name='one-t').pk
        version_name = 'three-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = []
        self.assertEquals(result, test)

    def test_versions_count_more_than_students_one_4(self):
        test_id = models.Test.objects.get(name='one-t').pk
        version_name = 'four-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = [('four-s', 'four-v', [1, 3])]
        self.assertEquals(result, test)

    def test_versions_count_more_than_students_one_5(self):
        test_id = models.Test.objects.get(name='one-t').pk
        version_name = 'five-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = []
        self.assertEquals(result, test)

    def test_versions_count_more_than_students_one_6(self):
        test_id = models.Test.objects.get(name='one-t').pk
        version_name = 'six-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = []
        self.assertEquals(result, test)

    def test_versions_count_more_than_students_one_no_version(self):
        test_id = models.Test.objects.get(name='one-t').pk
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id,))
        result = cursor.fetchall()
        test = [
            ('four-s', 'four-v', [1, 3]),
            ('one-s', 'two-v', [2]),
        ]
        self.assertEquals(result, test)

    def test_versions_count_less_than_students_one_1(self):
        test_id = models.Test.objects.get(name='three-t').pk
        version_name = '3-3-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = []
        self.assertEquals(result, test)

    def test_versions_count_less_than_students_one_2(self):
        test_id = models.Test.objects.get(name='three-t').pk
        version_name = '2-3-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = [('two-s', '2-3-v', [1])]
        self.assertEquals(result, test)

    def test_versions_count_less_than_students_one_4(self):
        test_id = models.Test.objects.get(name='three-t').pk
        version_name = '3-3-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = []
        self.assertEquals(result, test)

    def test_versions_count_less_than_students_one_5(self):
        test_id = models.Test.objects.get(name='three-t').pk
        version_name = '1-3-v'
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id, version_name))
        result = cursor.fetchall()
        test = [
            ('five-s', '1-3-v', [2, 3]),
            ('three-s', '1-3-v', [1, 2]),
        ]
        self.assertEquals(result, test)

    def test_versions_count_less_than_students_one_no_version(self):
        test_id = models.Test.objects.get(name='three-t').pk
        cursor = connection.cursor()
        cursor.callproc('get_missing_pages', (test_id,))
        result = cursor.fetchall()
        test = [
            ('five-s', '1-3-v', [2, 3]),
            ('three-s', '1-3-v', [1, 2]),
            ('two-s', '2-3-v', [1]),
        ]
        self.assertEquals(result, test)

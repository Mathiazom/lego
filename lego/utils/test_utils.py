import asyncio

from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase, APITransactionTestCase


class BaseTestCase(TestCase):
    pass


class BaseAPITestCase(APITestCase):
    pass


class BaseAPITransactionTestCase(APITransactionTestCase):
    pass


class ViewTestCase(BaseTestCase):
    def assertStatusCode(self, response, code=200):
        self.assertEqual(response.status_code, code)


def fake_time(y, m, d):
    dt = timezone.datetime(y, m, d)
    dt = timezone.pytz.timezone("UTC").localize(dt)
    return dt


def async_test(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)

    return wrapper

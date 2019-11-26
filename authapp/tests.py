from django.test import TestCase
from authapp.models import registers, signin


# Create your tests here.
class logintestcase(TestCase):
    def setUp(self):
        signin.objects.create(email='hii@gmail.com', Password='hello')

    def test_signin_info(self):
        s1 = signin.objects.get(email='hii@gmail.com', Password='hello')
        self.assertEqual(s1.get_user(), "hii@gmail.com")
        self.assertEqual(s1.get_pswd(), "hello")


class registersTestCase(TestCase):
    def setUp(self):
        registers.objects.create(email='hii', Password='hello')

    def test_signin_info(self):
        s1 = registers.objects.get(email='hii', Password='hello')
        self.assertEqual(s1.get_user(), 'man')
        self.assertEqual(s1.get_pswd(), 'man oj')

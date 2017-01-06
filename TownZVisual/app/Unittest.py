from django.test import TestCase

class Unittest(TestCase):
    def setUp(self):
        self.client.login(username='admin', password='geheim12345')

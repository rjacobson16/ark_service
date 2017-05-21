from django.test import TestCase

from arkapp.models import *
# Create your tests here.

class MinterTestCase(TestCase):
	def testMint(self):
		prev_num_arks = len(Ark.objects.all())
		testMinter = Minter(name="testMinter", template ="ddeeddteek", prefix="12345")
		testMinter.save()
		testMinter.mint(3)

		self.assertEqual(len(Ark.objects.all()), prev_num_arks + 3)

	def testArkExists(self):
		testMinter = Minter(name="testMinter", template ="ddeeddteek", prefix="12345")
		testMinter.save()
		testArk = Ark.objects.create(key='77777', minter = testMinter)

		self.assertEqual(testMinter._ark_exists('77777'), True)

class ArkTestCase(TestCase):


	def testBind(self):
		testMinter = Minter(name="testMinter", template ="ddeeddteek", prefix="12345")
		testMinter.save()
		testArk = Ark.objects.create(key='99999', minter = testMinter)

		testArk.bind('www.google.com')
		self.assertEqual(testArk.url, 'www.google.com')

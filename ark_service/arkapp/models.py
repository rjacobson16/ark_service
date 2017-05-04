from django.db import models
from django.conf import settings
import arkpy
# Create your models here.

class Minter(models.Model):
	name = models.CharField(max_length=256)
	prefix = models.CharField(max_length=7)
	template = models.CharField(max_length=25)
	active = models.BooleanField(default=True)
	date_created = models.DateField(auto_now_add=True)
	description = models.TextField()

	def __repr__(self):
		return '<Minter: {}'.format(self.name)

	def __str__(self):
		return self.name

	def _ark_exists(self, key):
		return (Ark.objects.filter(key=key).exists())


	def mint(self, quantity):

		i = 0
		while i < quantity:
			key = arkpy.mint(authority=settings.NAAN, prefix=self.prefix, template=self.template)
			if self._ark_exists(key):
				continue
			else:
				Ark.objects.create(key=key, minter = self)
				i+=1


class Ark(models.Model):
	key = models.CharField(max_length=25, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	minter = models.ForeignKey(Minter)
	url = models.URLField(null=True, blank=True)

	def __repr__(self):
		return '<Ark: {}>'.format(self.key)

	def __str__(self):
		return 'ARK# ' + self.key	

	def bind(self, url):
		self.url = url

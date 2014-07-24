from django.db import models
from django.contrib.auth import get_user_model

class Product(models.Model):
	name = models.CharField(
		max_length = 50,
		unique = True,
		help_text = 'The name of the product.'
	)

	def __unicode__(self):
		return self.name

class SKU(models.Model):
	name = models.CharField(
		max_length = 75,
		unique = True,
		help_text = 'The name of the SKU.'
	)

	product = models.ForeignKey(Product)

	def __unicode__(self):
		return self.name

	class Meta():
		verbose_name = "SKU"

class Key(models.Model):
	key = models.CharField(
		max_length = 140,
		help_text = 'The key text.'
	)

	key_type = models.CharField(
		max_length = 50,
		help_text = 'The type of key, as reported by the MSDNAA portal.'
	)

	allocated_to = models.ForeignKey(get_user_model(),
		blank = True,
		null = True,
		help_text = "The user the key has been allocated to.",
		related_name = 'allocated_to'
	)

	allocated_by = models.ForeignKey(get_user_model(),
		blank = True,
		null = True,
		help_text = "The user that allocated this key.",
		related_name = 'allocated_by'
	)

	allocated_at = models.DateTimeField(
		blank = True,
		null = True,
		help_text = "The time and date at which the key was allocated, if at all."
	)

	imported_by = models.ForeignKey(get_user_model(),
		related_name = 'imported_by'
	)
	
	sku = models.ForeignKey(SKU)

	class Meta():
		unique_together = ['key', 'sku']

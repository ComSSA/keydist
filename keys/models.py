from __future__ import division
from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy

class Product(models.Model):
    name = models.CharField(
        max_length = 50,
        unique = True,
        help_text = 'The name of the product.'
    )

    @property
    def total_keys(self):
        total = 0
        for sku in self.sku_set.all():
            total += sku.key_set.count()

        return total

    @property
    def total_unallocated_keys(self):
        total = 0
        for sku in self.sku_set.all():
            total += sku.key_set.filter(allocated_to = None).count()

        return total

    def get_absolute_url(self):
        return reverse_lazy('keys:product-detail', args = [self.id])
        
    def __unicode__(self):
        return self.name

    class Meta():
        ordering = ['name']

class SKU(models.Model):
    name = models.CharField(
        max_length = 75,
        unique = True,
        help_text = 'The name of the SKU.'
    )

    product = models.ForeignKey(Product)

    def __unicode__(self):
        return self.name

    @property
    def unallocated_keys(self):
        return self.key_set.filter(allocated_to = None)

    @property
    def nearing_exhaustion(self):
        if self.key_set.all().count() != 0:
            return (self.key_set.exclude(allocated_to = None).count() / self.key_set.all().count()) >= 0.90
        else:
            return True
    class Meta():
        verbose_name = "SKU"
        ordering = ['name']

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

    imported_at = models.DateTimeField(
        help_text = "The date and time at which the key was imported."
    )
    
    sku = models.ForeignKey(SKU)

    def get_absolute_url(self):
        return reverse_lazy('keys:detail', args = [self.id])

    def __unicode__(self):
        return "Key for %s" % self.sku.name

    class Meta():
        unique_together = ['key', 'sku']

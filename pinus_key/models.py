from django.db import models
from enum import Enum
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType




# Create your models here.
class Distribution(Enum):
    NORTH = 'Northern states'
    MIDDLE = 'Middle states'
    SOUTH = 'south'
    NORTH_MIDDLE = 'northern and middle states'
    MIDDLE_SOUTH = 'middle and southern states'


class NeedleCount(Enum):
    TWO = 2
    THREE = 3
    FIVE = 5


class NeedleLength(Enum):
    TWO_THREE = '2-3',
    TWO_FOUR = '2-4',
    THREE_FIVE = '3-5',
    THREE_SIX = '3-6',
    FOUR_SIX = '4-6',
    FOUR_EIGHT = '4-8',
    FIVE_ELEVEN = '5-11',
    SIX_NINE = '6-9',
    EIGHT_EIGHTEEN = '8-18',


class ConeLength(Enum):
    LARGE = 'longer than three inches'
    SHORT = 'shorter than three inches'
    BOTH = 'size can be plus or minus 3 inches'


class ConeShape(Enum):
    ROUND = 'round'
    LONG = 'Longer than Wide'
    WIDE = 'Wider than long'
    BOTH = 'larger axis varies'


class ConePrickles(Enum):
    THIN = 'thin'
    LACKING = 'lacking'
    THIN_LACKING = 'thin to lacking'
    STOUT = 'stout'


class PinusGenus(models.Model):
    NEEDLE_LENGTH_CHOICES = [(key.value, key.value.title())
                             for key in NeedleLength]
    NEEDLE_COUNT_CHOICES = [(key.value, key.value.title())
                            for key in NeedleCount]
    CONE_LENGTH_CHOICES = [(key.value, key.value.title())
                           for key in ConeLength]
    CONE_SHAPE_CHOICES = [(key.value, key.value.title()) for key in ConeShape]
    CONE_PRICKLES_CHOICES = [(key.value, key.value.title())
                             for key in ConePrickles]
    DISTRIBUTION_CHOICES = [(key.value, key.value.title())
                            for key in Distribution]
    common_name = models.CharField(max_length=150)
    scientific_name = models.CharField(max_length=150)
    summary = models.CharField(max_length=5000)
    old_cones = models.BooleanField()
    twig_texture = models.BooleanField()
    fire_resilience = models.BooleanField()
    distribution = models.CharField(choices=DISTRIBUTION_CHOICES )
    needle_length  = models.CharField(choices = NEEDLE_LENGTH_CHOICES )
    needle_count = models.IntegerField(choices = NEEDLE_COUNT_CHOICES )
    cone_length = models.CharField(choices = NEEDLE_LENGTH_CHOICES )
    cone_shape = models.CharField(choices = CONE_SHAPE_CHOICES )
    cone_prickles = models.CharField(choices = CONE_PRICKLES_CHOICES )

class PinusKey(models.Model):
  characteristic_a = models.CharField(max_length=400)
  characteristic_b = models.CharField(max_length=400)
  parent= models.ForeignKey('self', on_delete=models.PROTECT)
  child_a = models.ForeignKey(ContentType)
  child_b = models.ForeignKey(ContentType)
  object_id = models.PositiveIntegerField()
  choose_a = GenericForeignKey('child_a', 'object_id') 
  choose_b = GenericForeignKey('child_b', 'object_id')
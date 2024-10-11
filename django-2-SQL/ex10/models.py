from django.db import models
from django.utils import timezone

# Create your models here.
class Planets(models.Model):
	name=models.CharField(max_length=64, unique=True)
	climate=models.CharField(null=True)
	diameter=models.IntegerField(null=True)
	orbital_period=models.IntegerField(null=True)
	population=models.BigIntegerField(null=True)
	rotation_period=models.IntegerField(null=True)
	surface_water=models.FloatField(null=True)
	terrain=models.CharField(null=True)
	created=models.DateTimeField(auto_now_add=True, null=True)
	updated=models.DateTimeField(auto_now=True, null=True)

	def save(self, *args, **kwargs):
        # Ensure `created` is set when missing (useful for loading data)
		if not self.created:
			self.created = timezone.now()
		if not self.updated:
			self.updated = timezone.now()
		super(Planets, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class People(models.Model):
	name=models.CharField(max_length=64)
	birth_year=models.CharField(max_length=32, null=True)
	gender=models.CharField(max_length=32, null=True)
	eye_color=models.CharField(max_length=32, null=True)
	hair_color=models.CharField(max_length=32, null=True)
	height=models.IntegerField(null=True)
	mass=models.FloatField(null=True)
	homeworld=models.ForeignKey(Planets, related_name='planet', on_delete=models.SET_NULL, null=True)
	created=models.DateTimeField(auto_now_add=True, null=True)
	updated=models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name

class Movies(models.Model):
	title = models.CharField(max_length=64, unique=True)  # Unique, 64-byte max, non-null
	episode_nb = models.BigAutoField(primary_key=True)  # Full, primary key
	opening_crawl = models.TextField(null=True, blank=True)  # Text, can be null, no size limit
	director = models.CharField(max_length=32)  # 32-byte max, non-null
	producer = models.CharField(max_length=128)  # 128-byte max, non-null
	release_date = models.DateField()  # Date, non-null
	characters = models.ManyToManyField(People)
	# created = models.DateTimeField(auto_now_add=True)
	# updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

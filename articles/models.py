from django.db import models
from django.contrib.auth.models import User


class articles(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(auto_now=True)
	title = models.CharField(max_length=200)
	brief_content = models.TextField(default="A brief (Old French from Latin 'brevis', short) is a written legal document used in various legal adversarial systems that is presented to a court arguing why one party to a particular case should prevail....")
	content = models.TextField()
	no_of_reads = models.IntegerField(default=0)
	image = models.ImageField(default="images.jpg", blank=True)
	read_time = models.IntegerField()
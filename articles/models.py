from django.db import models
from django.contrib.auth.models import User


class tags(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class articles(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(auto_now=True)
	title = models.CharField(max_length=200)
	brief_content = models.TextField(default="A brief (Old French from Latin 'brevis', short) is a written legal document used in various legal adversarial systems that is presented to a court arguing why one party to a particular case should prevail")
	content = models.TextField()
	no_of_reads = models.PositiveIntegerField(default=0)
	likes = models.PositiveIntegerField(default=0)
	image = models.ImageField(default="images.jpg", blank=True)
	read_time = models.IntegerField()
	tags = models.ManyToManyField(tags)
	
	def __str__(self):
		return self.title + str(self.pk)


class read_info(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="read_user")
	article = models.ForeignKey(articles, on_delete=models.CASCADE)

	def __str__(self):
		return self.article.title + str(self.article.pk) + "by" + self.user.username

class starred_info(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="starred_user")
	article = models.ForeignKey(articles, on_delete=models.CASCADE)

	def __str__(self):
		return self.article.title + str(self.article.pk) + "by" + self.user.username



from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
	name = models.CharField(max_length=100,null=False,blank=False)

	def __str__(self):
		return self.name

class News(models.Model):
	title = models.CharField(max_length=250,null=False,blank=False)
	image = models.ImageField(upload_to="images/",blank=True)
	text = RichTextField()
	category = models.ForeignKey(Category,blank=False,null=True,on_delete=models.SET_NULL)
	category_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title



class ListView_Kod(models.Model):
	name1 = models.CharField(max_length=100,null=False,blank=False)
	name2 = models.TextField()

	def __str__(self):
		return self.name1


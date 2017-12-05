from django.db import models

# Create your models here.
class Topic(models.Model):
  top_name = models.CharField(max_length=264,unique=True)

  def __str__(self):
    return self.top_name

class Webpage(models.Model):
  # In Tuts, on_delete not mentioned => necessary!
  topic = models.ForeignKey(Topic,on_delete=models.CASCADE,)
  name = models.CharField(max_length=264,unique=True)
  url = models.URLField(unique=True)

  def __str__(self):
    return self.name

class AccessRecord(models.Model):
  # In Tuts, on_delete not mentioned => necessary!
  name = models.ForeignKey(Webpage,on_delete=models.CASCADE,)
  date = models.DateField()

  def __str__(self):
    return str(self.date)
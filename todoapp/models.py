from django.db import models

# Create your models here.
class Todo(models.Model):
  todo = models.CharField(max_length = 100)
  status = models.BooleanField(default= False)
  date_added = models.DateTimeField(auto_now_add = True)
  # date_completed = models.DateTimeField(auto_now = True, default = False)
  
  def __str__(self): return self.todo
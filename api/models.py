from django.db import models

# Create your models here.
class Student(models.Model):
    age = models.CharField(u'age', max_length=10, default='0')
    name = models.CharField(u'name', max_length=100, default='no_name')

    def __unicode_(self):
        return '%d: %s' % (self.pk, self.name)



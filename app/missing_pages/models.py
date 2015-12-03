from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'{}'.format(self.name)
































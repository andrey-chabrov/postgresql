from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Test(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Version(models.Model):
    test = models.ForeignKey(Test)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('test', 'name',)
        ordering = ('test__name',)

    def __unicode__(self):
        return u'test {}: {}'.format(unicode(self.test), self.name)


class Page(models.Model):
    version = models.ForeignKey(Version)
    index = models.IntegerField()

    class Meta:
        unique_together = ('version', 'index',)
        ordering = ('version__test__name', 'version__name', 'index',)

    def __unicode__(self):
        return u'version {}: {}'.format(unicode(self.version), self.index)

class StudentPage(models.Model):
    page = models.ForeignKey(Page)
    student = models.ForeignKey(Student)
    status = models.IntegerField()

    class Meta:
        unique_together = ('page', 'student',)
        ordering = ('student__name', 'page__version__test__name',
            'page__version__name', 'page__index',)

    def __unicode__(self):
        return u'page {}, student {}: status {}'.format(
            unicode(self.page), unicode(self.student), self.status)

from django.db import models

class Talk(models.Model):
    title = models.CharField('Title', max_length=200)
    seminar_name = models.CharField('Seminar Name', max_length=200)
    location = models.CharField('Location', max_length=200)
    date_given = models.DateField('Date Given')
    abstract = models.TextField('Abstract', blank = True)
    
    def __str__(self):
        return self.title

class Paper(models.Model):
    title = models.CharField('Title',max_length=400)
    authors = models.TextField('Authors')
    link = models.URLField('Link', null = True)
    pub_date = models.DateField('Date Published')
    cite = models.CharField('Citation', max_length=500)
    
    def __str__(self):
        return self.title

class Award(models.Model):
    title = models.CharField('Title',max_length=400)
    date_obt = models.DateField('Date Obtained')
    text = models.TextField('Text on award', blank = True)
    organisation_name = models.CharField('Organisation', max_length=200)
    organisation_URL = models.URLField('Organisation URL', null=True)
    
    def __str__(self):
        return self.title
        
class Teaching(models.Model):
    
    class LevelChoices(models.TextChoices):
        GCSE = 'GC', 'GCSE'
        ALevel = 'AL', 'A-Level'
        Undergrad_year_1 = 'U1', 'Undergraduate Year 1'
        Undergrad_year_2 = 'U2', 'Undergraduate Year 2'
        Undergrad_year_3 = 'U3', 'Undergraduate Year 3'
        Masters = 'MA', 'Masters'
    
    level = models.CharField(
        max_length=2,
        choices = LevelChoices.choices,
        default = LevelChoices.Undergrad_year_1
    )
    
    class TypeChoices(models.TextChoices):
        Tutor = 'TU', 'Tutor'
        Supervisor = 'SU', 'Supervisor'
        ClassTeacher = 'CT', 'Class Teacher'
        Lecturer = 'LE', 'Lecturer'
    
    type = models.CharField(
        max_length=2,
        choices = TypeChoices.choices,
        default = TypeChoices.ClassTeacher
    )
    
    title = models.CharField('Title', max_length=200)
    organisation_name = models.CharField('Organisation', max_length=200)
    organisation_URL = models.URLField('Organisation URL')
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End date')
    description = models.TextField('Description')
    
    def __str__(self):
        return self.level + ' - ' + self.type + ': ' + self.title + ' for ' + self.organisation_name
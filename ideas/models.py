from django.db import models

class Idea(models.Model):
    title = models.CharField('Title', max_length=200)
    date_thought = models.DateField('Date Thought')
    Explaination = models.TextField('Explanation', blank = True)
	
    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    """A Tag linked to a question."""
    text = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=300,null=True,blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Return a string representation of model."""
        return self.text
    
class Question(models.Model):
    """Questions related to a Topic."""
    tag = models.ForeignKey(Tag,on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User,on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'

    def __str__(self):
        """Return String."""
        if len(self.text) > 150:
            return self.text[:150] + "..."
        else:
            return self.text

class Answer(models.Model):
    """Answe to a particular Question."""
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User,on_delete=models.PROTECT)
    rating = models.PositiveIntegerField()

    def __str__(self):
        """Return String Representation."""
        if len(self.text) > 250:
            return self.text[:250] + "..."
        else:
            return self.text



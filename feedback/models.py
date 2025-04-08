from django.db import models
from textblob import TextBlob

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    comment = models.TextField()
    sentiment = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.course.name} - {self.sentiment}"
    
def save(self, *args, **kwargs):
    analysis = TextBlob(self.comment)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        self.sentiment = 'Positive'
    elif polarity < 0:
        self.sentiment = 'Negative'
    else:
        self.sentiment = 'Neutral'
    super().save(*args, **kwargs)


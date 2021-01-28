from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    data_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Quizzes"


class Update(models.Model):#diğer modellerde aynısı olduğu için ortak class oluşturup diğer class tan inherit ettik
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True #database e kaydetme demek
    
    
class Question(Update):
    
    Scale = (
        (0, "Beginner"),
        (1, "Intermediate"),
        (2, "Advance")
    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name="question")
    difficulty = models.IntegerField(choices=Scale)
    date_create = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
class Answer(Update):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=250)
    is_right = models.BooleanField(default=False)
    
     
    
    
    
    
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
    
    @property    #attribute olarak kullanmamızı sağlar. sonuna parantez koymadan veri alabiliriz. zorunlu değil
    def quiz_count(self):
        return self.quiz_set.count()
    

class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    data_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Quizzes"
    
    @property    #attribute olarak kullanmamızı sağlar. sonuna parantez koymadan veri alabiliriz. zorunlu değil
    def question_count(self):
        return self.question_set.count()


class Update(models.Model):#diğer modellerde aynısı olduğu için ortak class oluşturup diğer class tan inherit ettik
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True #database e kaydetme demek
    
    
class Question(Update):
    
    SCALE = (
        (0, "Beginner"),
        (1, "Intermediate"),
        (2, "Advanced")
    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name="question")
    difficulty = models.IntegerField(choices=SCALE)
    date_create = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
class Answer(Update):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer') #related_name='answer' YAZMAZSAK answer json da gözükmüyor
    answer_text = models.CharField(max_length=250)
    is_right = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer_text
    
     
    
    
    
    
from django.contrib import admin
import nested_admin
from .models import Category,Quiz,Question,Answer

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    # sortable_field_name = "position"
    extra = 2  #fazladan Answer soru hanesi
    max_num = 5 #maksimum seçenek/şık (Answer Text) hakkı

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline]
    
    
class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]   
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)

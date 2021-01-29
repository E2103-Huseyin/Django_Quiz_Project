from rest_framework import serializers
from .models import Category,Quiz,Question,Answer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "quiz_count"
        )

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            "title",
            
            "question_count"
        )
        

class AnswerSerializer(serializers.ModelSerializer):
    #models.py dosyasına related_name='answer' YAZMAZSAK answer json da gözükmüyor
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer_text',
            'is_right',
        )
                
            
    
class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    #SCALE = ( (0, "Beginner"), (1, "Intermediate"), (2, "Advanced")  burada difficulty değerini 0,1,2 değil de Advanced/Intermediate/Beginner olarak gösterebilmek için:
    #serializers.SerializerMethodField() özel method kullanılır
    difficulty = serializers.SerializerMethodField()
    
    
    
    class Meta:
        model = Question
        fields = (
            "title",
            "answer",
            "difficulty",
        )
        
    def get_difficulty(self, obj):
        return obj.get_difficulty_display()
    #data base adı değil de frontend adını göstermek istiyorsak:
    #.get_FILENAME_display() kullanılır
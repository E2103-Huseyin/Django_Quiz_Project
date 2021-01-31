from django.shortcuts import render
from rest_framework import generics
from .models import Category,Quiz,Question
from .serializers import CategorySerializer,CategoryDetailSerializer,QuestionSerializer
from .paginations import MyPagination
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]
    
class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Category.objects.all()
    
    def get_queryset(self):
        queryset= Quiz.objects.all()
        category = self.kwargs["category"]
        queryset = queryset.filter(category__name=category)
        return queryset
        

class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset= Question.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(quiz__title=title)
        return queryset
       
    
from django.shortcuts import render,redirect
from .models import Question
# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    user = request.GET.get('user')
    title = request.GET.get('title')
    content = request.GET.get('content')

    question = Question()
    question.title = title
    question.user = user
    question.content = content
    question.save()

    return redirect('/questions/')

def index(request):
    questions = Question.objects.all()#전체데이터 가져와
    context = {
        'questions' : questions
    }
    return render(request, 'index.html', context)
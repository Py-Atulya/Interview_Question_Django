from django.shortcuts import render

from Api.models import QuestionModel
def index(request):
    javascript_title = "JavaScript Interview Question 2025"
    python_title = "Python Interview Question 2025"
    question = QuestionModel.objects.all()

    for que in question:
        print(que.language)

    dict = {'javascript_title': javascript_title,'python_title':python_title,'question': question}
    return  render(request,'index.html',dict)

def javascript(request):
    javascript_title = "JavaScript Interview Question 2025"
    question = QuestionModel.objects.all()
    dict = {'javascript_title': javascript_title, 'question': question}
    return render(request,'JavaScript.html',dict)


def python(request):
    python_title = "Python Interview Question 2025"
    question = QuestionModel.objects.all()
    dict = {'python_title': python_title, 'question': question}
    return render(request,'Python.html',dict)


def home(request):
    question = QuestionModel.objects.all()
    dict = {'question': question}
    return render(request,'home.html',dict)


def django(request):
    django_title = "Django Interview Question 2025"
    question = QuestionModel.objects.all()
    dict = {'django_title': django_title, 'question': question}
    return render(request,'django.html',dict)

def react(request):
    react_title = "React Interview Question 2025"
    question = QuestionModel.objects.all()
    dict = {'react_title': react_title, 'question': question}
    return render(request,'react.html',dict)

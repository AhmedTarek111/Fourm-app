from django.shortcuts import render,redirect
from django.views.generic import DeleteView
from .models import Question, Answer
from .forms import *

def all_questions(request):
    '''
    this function can:
      display : questions with thiers answers 
      add answer for spcefic queistons
      delete the question 
      delete the answer 

    '''
    if request.method == 'POST':
        answer_form = Answerform(request.POST)
        question = request.POST.get('question')  
        if answer_form.is_valid():
            my_answer_form = answer_form.save(commit=False)
            my_answer_form.author = request.user
            questionn = Question.objects.get(question=question)  
            my_answer_form.question = questionn  
            my_answer_form.save()
    else:
        answer_form = Answerform()

    answers = Answer.objects.all()
    questions = Question.objects.all()

    
    return render(request, 'all_questions.html', {'questions': questions, 'answers': answers, 'answer_form': answer_form})

def create_question(request):
    if request.method == 'POST':
        form = Questionform(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('/main/')

    else:
        form = Questionform()
    return render(request, 'add_question.html', {"form": form})



class DeleteQuestion(DeleteView):
    model = Question
    template_name = 'delete_question.html'
    success_url = '/main/'

class DeleteAnswer(DeleteView):
    model = Answer
    template_name = 'delete_answer.html'
    success_url = '/main/'
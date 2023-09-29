from django.shortcuts import render,redirect
from django.views.generic import DeleteView,UpdateView
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
    answers = Answer.objects.all()
    questions = Question.objects.all()
    
    if request.method == 'POST':
        answer_form = Answerform(request.POST)
        question = request.POST.get('question')  #to get the question that belong to the Question model from the template 
        if answer_form.is_valid():
            my_answer_form = answer_form.save(commit=False)
            my_answer_form.author = request.user
            questionn = Question.objects.get(question=question) # to get the question from the Question model that is the same in the model
            my_answer_form.question = questionn  # to fill the question field that belong to the Answer model and to make the Answer is to the right question 
            my_answer_form.save()
    else:
        answer_form = Answerform()

    context={'questions': questions,
               'answers': answers,
               'answer_form': answer_form,
               }
    
    return render(request, 'all_questions.html', context)

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

class Editquestion(UpdateView):
    model =Question
    fields =['question','content','tags']
    template_name = 'edit_question.html'
    success_url = '/main/'

class Editanswer(UpdateView):
    model =Answer
    fields =['answer',]
    template_name = 'edit_question.html'
    success_url = '/main/'


    
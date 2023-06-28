from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sobre(request):
    return HttpResponse('Este é um app de enquete!')

def exibe_questao(request, question_id):
    questao = Question.objects.get(id=question_id)
    # questao.question_text
    return HttpResponse(questao.question_text)

def ultimas_perguntas(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
   # return render(request, 'polls/perguntas.html', context)
    return render(request, 'perguntas_recentes.html', context)
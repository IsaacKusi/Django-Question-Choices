from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
#from django.http import Http404
#from django.template import loader

from .models import Choices, Question


class IndexView (generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self) :
        return Question.objects.filter( pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # # return HttpResponse(template.render(context, request))
    # return render(request, 'polls/index.html', context)




# def detail(request, question_id):
#     # try :
#     #     question = Question.objects.get(pk=question_id)

#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not Exist')

#     question = get_object_or_404(Question, pk=question_id)
     
#     return render(request,'polls/results.html', {
#             'question' : question
#         } )

# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/results.html', {'question': question} )

class DetailView (generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView (generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices_set.get(pk = request.POST['choices'])
    except (KeyError,Choices.DoesNotExist):
        return render (request, 'polls/details.html',{'question': question, 'error_message': 'you did not select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))






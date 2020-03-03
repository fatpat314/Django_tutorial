from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
# from django.template import loader
# from django.http import http404
# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render
from .models import Choice, Question
from django.utils import timezone
from .forms import FriendlyForm, QuestionCreateForm
from django.views.generic.edit import CreateView


def form_demo(request):
    form = FriendlyForm()
    context = { 'form': form }
    return render(request, 'polls/form_demo.html', context)

class QuestionCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': QuestionCreateForm()}
        return render(request, 'polls/new.html', context)

    def post(self, request, *args, **kwargs):
        form = QuestionCreateForm(retuest.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(reverse_lazy('polls:detail',args=[question.id]))
        return render(request, 'polls/new.html', {'form': form})





class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions. """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        # return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_massage': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

    return HttpResponseRedirect(reverse('polls:results', args=(question.id)))





# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list}
#
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise http404("Question does not exist")
#
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse("You're looking at question %s." % question_id)
#
#
#
# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     question = get_object_or_404(Question, pk=question_id)
#     # return HttpResponse(response % question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_massage': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes +=1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id)))

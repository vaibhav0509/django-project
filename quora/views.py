from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required

from .models import Tag, Question, Answer
from .forms import TagForm, QuestionForm, AnswerForm

def index(request):
    """The home page for Quora"""
    questions = Question.objects.order_by('-id')
    answers = Answer.objects.order_by('-rating')
    qa = {}
    for q in questions:
        qa[int(q.id)] = 'No Answer.'
        for a in answers:
            if a.question == q:
                qa[int(q.id)] = a.text
                break
    questions = Question.objects.order_by('-date_added')
    context = {'questions':questions,'qa':qa}
    return render(request, 'quora/index.html',context)

def tags(request):
    """Show all tags."""
    tags = Tag.objects.order_by('text')
    context = {'tags': tags}
    return render(request, 'quora/tags.html',context)

def tag(request, tag_id):
    """Show a single tag and all its questions."""
    tag = Tag.objects.get(id=tag_id)
    questions = tag.question_set.order_by('-date_added')
    context = {'tag':tag, 'questions':questions}
    return render(request, 'quora/tag.html', context)

@login_required
def new_tag(request):
    """Add a new tag."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TagForm()
    else:
        # POST data submitted; process data.
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('quora:tags'))
    context = {'form':form}
    return render(request, 'quora/new_tag.html',context)

def question(request, question_id):
    """Show Question With its answers."""
    question = Question.objects.get(id=question_id)
    #answers = Answer.objects.get(question=question)
    answers = question.answer_set.order_by('-rating')
    context = {'question':question, 'answers':answers}
    return render(request, 'quora/question.html', context)



@login_required
def new_question(request, tag_id=1):
    """Adding a new Question to a particular tag."""
    #tag = Tag.objects.get(id=tag_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = QuestionForm()
        form.fields['tag'].initial = tag_id 
    else:
        # POST data submitted; process data.
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            #new_question.tag = tag
            new_question.owner = request.user
            new_question.save()
            return HttpResponseRedirect(reverse('quora:tag',args=[new_question.tag.id]))
    
    context = {'form':form}
    return render(request, 'quora/new_question.html', context)

@login_required
def edit_question(request, question_id):
    """Edit an existing question."""
    question = Question.objects.get(id=question_id)
    tag = question.tag
    if question.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry.
        form = QuestionForm(instance=question)

    else:
        # POST data submitted; process data.
        form = QuestionForm(instance=question, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('quora:tag', args=[tag.id]))
    
    context = {'question': question, 'tag':tag, 'form':form}
    return render(request, 'quora/edit_question.html', context)

@login_required
def answer_question(request, question_id):
    """Answering a particular question."""
    question = Question.objects.get(id=question_id)
    tag = question.tag

    if request.method != 'POST':
        # Initial request; pre-fill form with question and answers.
        form = AnswerForm()

    else:
        # POST data submitted; process data.
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.owner = request.user
            new_answer.rating = 1
            new_answer.question = question
            new_answer.save()
            # change redirect page
            #return HttpResponseRedirect(reverse('quora:index'))
            return HttpResponseRedirect(reverse('quora:question',args=[question_id]))

    context = {'question':question, 'form':form, 'tag':tag}
    return render(request, 'quora/answer_question.html', context)

        
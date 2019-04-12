"""Defines URL patterns for quora."""

from django.urls import include,path
from . import views

app_name = 'quora'

urlpatterns = [
    # Home page
    path('',views.index, name='index'),

    # Show all tags.
    path('tags',views.tags, name='tags'),

    # All Question in a single tag.
    path('tags/<int:tag_id>/', views.tag, name='tag'),

    # Page for adding a new tag.
    path('new_tag', views.new_tag, name='new_tag'),

    # Page for adding a new question.
    path('new_question',views.new_question, name='new_question'),
    path('new_question/<int:tag_id>/',views.new_question, name='new_question_tag'),

    # Page for showing question and answer.
    path('question/<int:question_id>/', views.question, name='question'),

    # Page for editing questions.
    path('edit_question/<int:question_id>/',views.edit_question,name='edit_question'),

    # Page for answering question.
    path('answer_question/<int:question_id>/', views.answer_question,name='answer_question'),
    

]
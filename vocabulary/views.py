import random

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import generic

from vocabulary import models as md


class WordListView(generic.ListView):
    template_name = 'vocabulary/index.html'
    context_object_name = 'words_list'

    def get_queryset(self):
        return md.Word.objects.order_by('-added_date')[:20]


def study(request):
    words = md.Word.objects.all()
    list_ids = [item.id for item in words]
    english_word_for_guess = words.get(id=random.sample(list_ids, 1)[0])
    list_chosen = random.sample(list_ids, 4)
    list_chosen.insert(random.randint(1, 5), english_word_for_guess.id)
    variants = [words.get(id=item).russian_word for item in list_chosen]

    return render(request, 'vocabulary/study.html', {
        'english_word_for_guess': english_word_for_guess,
        'variants': variants,
    })


def test(request, pk):
    try:
        word = md.Word.objects.get(id=pk)
    except:
        return HttpResponseRedirect(reverse('vocabulary:study'))

    message = f'{word.english_word} - {word.russian_word}'
    if word.russian_word == request.POST.get('test_info', None):
        message = f'Excellent! ' + message
    else: message = f'You are wrong(. The right answer is: ' + message
    messages.success(request, message)
    return HttpResponseRedirect(reverse('vocabulary:study'))


def add_word(request):
    word = md.Word(english_word=request.POST['english'], russian_word=request.POST['russian'])
    word.save()
    return HttpResponseRedirect(reverse('vocabulary:show_all'))

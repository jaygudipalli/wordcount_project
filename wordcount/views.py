import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contactinfo(request):
    return HttpResponse('Jay.gudipalli@mymail.com')


def count(request):
    text_entered = request.GET['text_entered']
    word_list = text_entered.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1  # increase the count of the word
        else:
            word_dictionary[word] = 1  # add the word to the dictionary

    sorted_dictionary = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'entered_text': text_entered,
                                          'count': len(word_list), 'sorted_dictionary': sorted_dictionary})


def about(request):
    welcome_text = 'This is word counter Website. Enter the text in the textbox on home page and hit submit'
    return render(request, 'about.html',{'welcome_text' : welcome_text})


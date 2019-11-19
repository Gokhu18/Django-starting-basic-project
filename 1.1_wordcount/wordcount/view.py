from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(req):
    return render(req, 'home.html', {'status': 'django is awesome'})


def count(req):
    text = req.GET['inputArea']
    textInList = text.split(' ')
    totalWords = len(textInList)
    wordList = {}
    for w in textInList:
        if w in wordList:
            wordList[w] += 1
        else:
            wordList[w] = 1

    sortedWord = sorted(wordList.items(), key=operator.itemgetter(1), reverse=True)
    return render(req, 'count.html', {'text': text, 'wordCount': totalWords, 'wordlist': sortedWord})

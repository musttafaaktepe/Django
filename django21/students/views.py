from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    context = {
        'title': 'Clarusway',
        'desc': 'This is a description',
        'number': 1111,
        'list1': ['a', 1, 'b', ['c', 2]],
        'dict1': {
            'key1': 'value1',
            'key2': 'value2'
        }

    }

    return render(request, 'students/home.html', context)

    # return HttpResponse('<p> Hello </p>')


'''
{{ variables }}
{% command %}
'''

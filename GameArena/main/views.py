from django.template import loader
from django.http import HttpResponse, HttpRequest


def get_game(request: HttpRequest):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

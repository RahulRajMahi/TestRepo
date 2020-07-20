
#from django.views import View
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('<h1>Hello World Message from HelloWorld Class based view</h1>')

class HelloWorldTemplateView(TemplateView):
    template_name = 'testapp/results.html'

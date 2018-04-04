from django.shortcuts import render
from django.http import HttpResponse
from .models import Iris
from django.template.loader import get_template
# Create your views here.


def homepage(request):
    template =get_template('index.html')
    Data=Iris.objects.all()
    html = template.render(locals())
    '''
    for  count ,Data_ in enumerate(Data):
        Data_list.append("NO.{} ".format(str(count+1))\
                + str(Data_.sepal_length) +"<br>" \
                + str(Data_.sepal_width) +"<br>" \
                +  str(Data_.petal_length) +"<br>" \
                +  str(Data_.petal_width) +"<br>" \
                +  str(Data_.species) +"<br>" 
                +  "\n"
                )
                */
    '''
    return HttpResponse(html)

    

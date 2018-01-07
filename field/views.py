from django.shortcuts import render
from .models import Division

# Create your views here.


def index(request):
    d = Division.obj_with_count.all()
    conext = {'division': d}
    return render(request, 'field/index.html', context=conext)



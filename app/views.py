from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'HAi vibhu welcome to the new year','dt':dt,'c':1}
    return render(request,'filters.html',d)

def userdefinedfilters(request):
    d={'data':'HI vibhu welcome to the new year'}
    return render(request,'userdefinedfilters.html',d)

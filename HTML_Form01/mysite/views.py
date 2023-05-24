from django.shortcuts import render

# Create your views here.
def get_example(request):
    try:
        fcolor = request.GET['fcolor']
        fmovie = request.GET['fmovie']
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
        byear = request.GET['byear']
    except:
        urid = None

    
    if urid != None and urpass == '12345':
        verified = True
    else:
        verifeid = False
    
    years = range(1960,2023+1)
    return render(request, 'get_example.html', locals())
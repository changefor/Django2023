from django.shortcuts import render

# Create your views here.
def get_example(request):
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None
    
    if urid != None and urpass == '12345':
        verified = True
    else:
        verifeid = False

    return render(request, 'get_example.html', locals())
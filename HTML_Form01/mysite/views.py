from django.shortcuts import render
from mysite import models, forms

# Create your views here.
def index(request, pid=None, del_pass=None):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如要張貼訊息，則每一個欄位都要填...'
    
    if del_pass and pid:
        try:
            post = models.Post.objects.get(id=pid)
        except:
            post = None
        
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "資料刪除成功"
            else:
                message = "密碼錯誤"
    elif user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message='成功儲存！請記得你的編輯密碼[{}]!，訊息需經審查後才會顯示。'.format(user_pass)

    return render(request, 'index.html', locals())

def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'listing.html', locals())

def posting(request):
    moods = models.Mood.objects.all()
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
    except:
        user_id = None
        message = '如要張貼訊息，則每一個欄位都要填...'
    
    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message='成功儲存！請記得你的編輯密碼[{}]!，訊息需經審查後才會顯示。'.format(user_pass) 
        posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
        return render(request, 'listing.html', locals())
    return render(request, 'posting.html', locals())

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

def contact(request):
    form = forms.ContactForm()
    return render(request, 'contact.html', locals())

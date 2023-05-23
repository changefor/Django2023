import random
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from mysite.models import Product

# Create your views here.
def about(request):
    quotes = ['平凡的腳步也可以走完偉大的行程。',
    '每天醒來，敲醒自己的不是鐘聲，而是夢想。',
    '沒有口水與汗水，就沒有成功的淚水。',
    '別想一下造出大海，必須先由小河川開始。']
    quote = random.choice(quotes)
    return render(request, 'about.html', locals()) 

def listing(request):
    html = '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset='utf-8'>
        <title>商品列表</title>
        </head>
        <body>
        <h2>以下是目前本店販售中的產品列表</h2>
        <hr>
        <table width=400 border=1 bgcolor='#ccffcc'>
        {0}
        </table>
        <h2>以下是目前本店缺貨的</h2>
        <hr>
        <table width=400 border=1 bgcolor='#ccffcc'>
        {1}
        </table>
        </body>
        </html>
    '''
    
    products = Product.objects.filter(qty__gt=0).order_by('-price')
    tags = '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</td></tr>'.format(p.qty)
    
    
    products = Product.objects.filter(qty=0).order_by('-price')
    tags2 = '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in products:
        tags2 = tags2 + '<tr><td>{}</td>'.format(p.name)
        tags2 = tags2 + '<td>{}</td>'.format(p.price)
        tags2 = tags2 + '<td>{}</td></tr>'.format(p.qty)
    return HttpResponse(html.format(tags,tags2))


def listing2(request):
    products = Product.objects.filter(qty__gt=0).order_by('-price')
    return render(request, 'list.html', locals()) 

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
        #return HttpResponse('找不到指定的品項編號')
        #return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request, 'disp.html', locals())

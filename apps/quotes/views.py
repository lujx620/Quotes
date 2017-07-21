from django.shortcuts import render, redirect
from ..log_reg.models import Users
from ..quotes.models import Quotes
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Count, Q
# Create your views here.
def index(request):
    context={
        'user': Users.objects.get(id= request.session['log_user']),
        'quotes': Quotes.objects.all().exclude(favorite=request.session['log_user']),
        'fave_quotes':Quotes.objects.filter(favorite=request.session['log_user']),
    }
    return render(request, 'quotes/dashboard.html', context)

def q_process(request):
    result = Quotes.objects.validate(request.POST, request.session['log_user'])
    user= Users.objects.get(id= request.session['log_user'])

    if result[0] is True:
        for errs in result[1]:
            messages.error(request, errs)
    else:
        # Quotes.objects.create(quoter= request.POST['quoter'], content=request.POST['content'], user_id= user.id)
        return redirect(reverse ('quotes:index'))

def favorites(request, id):
    user = Users.objects.get(id = request.session['log_user'])
    favQuote = Quotes.objects.get(id=id)
    favQuote.favorite.add(user)
    return redirect(reverse('quotes:index'))

def remove(request, id):
    user= Users.objects.get(id= request.session['log_user'])
    removeQuote= Quotes.objects.get(id=id)
    removeQuote.favorite.remove(user)
    return redirect(reverse ('quotes:index'))

def users(request, id):
    #pass through id from user.id
    context= {
        'postee': Users.objects.get(id=id),
        'quotes': Quotes.objects.filter(user_id=id),
        'count': Users.objects.filter(id=id).annotate(num_count =Count('user')),
    }
    return render(request, 'quotes/user.html', context)

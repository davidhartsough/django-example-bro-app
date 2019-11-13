from django.shortcuts import render, redirect
from .models import Shout, Expression
from apps.login.models import Bro


def main(request):
    if 'broId' not in request.session:
        return redirect('/login')
    bro = Bro.objects.get(id=request.session['broId'])
    shouts = Shout.objects.all()
    expressions = Expression.objects.filter(bro=bro)
    context = {
        'shouts': shouts,
        'expressions': expressions
    }
    return render(request, 'main.html', context)


def shout(request):
    if 'broId' not in request.session:
        return redirect('/login')
    bro = Bro.objects.get(id=request.session['broId'])
    expression = Expression.objects.get(id=request.POST['expressionId'])
    Shout.objects.create(expression=expression, bro=bro)
    return redirect('/bro')


def new(request):
    if 'broId' not in request.session:
        return redirect('/login')
    if request.POST:
        text = request.POST['text']
        bro = Bro.objects.get(id=request.session['broId'])
        Expression.objects.create(text=text, bro=bro)
        return redirect('/bro')
    return render(request, 'new.html')

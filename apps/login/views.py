from django.shortcuts import render, redirect
import bcrypt
from .models import Bro


def router(request):
    if 'broId' in request.session:
        return redirect('/bro')
    return redirect('/login')


def login(request):
    if 'broId' in request.session:
        return redirect('/bro')
    error = False
    if request.POST:
        bros = Bro.objects.filter(broname=request.POST['broname'])
        if bros:
            bro = bros[0]
            if bcrypt.checkpw(request.POST['bropass'].encode('utf-8'), bro.bropass.encode()):
                request.session['broId'] = bro.id
                return redirect('/bro')
            else:
                error = "That wasn't your secret broword, bro."
        else:
            error = "There's no bro with that name, bro."
    return render(request, 'login.html', {'error': error})


def register(request):
    if 'broId' in request.session:
        return redirect('/bro')
    error = False
    if request.POST:
        broname = request.POST['broname']
        bros = Bro.objects.filter(broname=broname)
        if bros:
            error = "There's already a bro with that name, bro."
        else:
            bropass = request.POST['bropass'].encode('utf-8')
            pwhash = bcrypt.hashpw(bropass, bcrypt.gensalt()).decode('utf-8')
            bro = Bro.objects.create(broname=broname, bropass=pwhash)
            request.session['broId'] = bro.id
            return redirect('/bro')
    return render(request, 'register.html', {'error': error})


def logout(request):
    request.session.pop('broId')
    return redirect('/login')

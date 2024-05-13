from django.shortcuts import render, redirect

locked = True

# Create your views here.
def main(request):
    return render(request,'main.html')
def items(request): 
    return render(request, 'items.html')
def contacts(request): 
    return render(request, 'contacts.html')
def login(request):
    global locked
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        if login == 'admin' and password == '1234':
            locked = False
            return redirect('/account')
    return render(request, 'login.html')
def account(request):
    global locked
    if locked:
        return redirect('/login')
    return render(request, 'account.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse(
        """
        <div class='login-container'>
            <h2>Iniciar Sesión</h2>
            <form action='/login' method='POST'>
                <input type='text' name='username' placeholder='Usuario' required>
                <input type='password' name='password' placeholder='Contraseña' required>
                <input type='submit' value='Iniciar Sesión'>
            </form>
        </div>
        """
    )

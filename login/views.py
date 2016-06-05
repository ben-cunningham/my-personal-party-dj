from django.shortcuts import redirect


def login(request):
    
    return redirect('https://accounts.spotify.com/authorize?client_id=f3ee976a08f14c70bcb93f8bc020e019&redirect_uri=google')
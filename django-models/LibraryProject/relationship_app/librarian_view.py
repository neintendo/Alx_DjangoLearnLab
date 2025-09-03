from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_librarian(user):
    if user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=user)
            return profile.role == 'Librarian'
        except UserProfile.DoesNotExist:
            return False
    return False

@user_passes_test(is_librarian, login_url="/librarian/")
def admin_dashboard(request):
    context = {
        'title': 'Librarian Dashboard',
        'welcome_message': 'Welcome to the Librarian Dashboard!',
        'user': request.user
    }
    return render(request, 'librarian_view.html', context) # stub for now
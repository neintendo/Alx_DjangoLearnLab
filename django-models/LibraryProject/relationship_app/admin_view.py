from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_admin(user):
    if user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=user)
            return profile.role == 'Admin'
        except UserProfile.DoesNotExist:
            return False
    return False

@user_passes_test(is_admin, login_url="/admin/")
def admin_dashboard(request):
    context = {
        'title': 'Admin Dashboard',
        'welcome_message': 'Welcome to the Admin Dashboard!',
        'user': request.user
    }
    return render(request, 'admin_view.html', context) # stub for now
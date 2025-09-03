from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_member(user):
    if user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=user)
            return profile.role == 'Member'
        except UserProfile.DoesNotExist:
            return False
    return False

@user_passes_test(is_member, login_url="/member/")
def admin_dashboard(request):
    context = {
        'title': 'Member Dashboard',
        'welcome_message': 'Welcome to the Member Dashboard!',
        'user': request.user
    }
    return render(request, 'member_view.html', context) # stub for now
from django.shortcuts import render
from Subjects.views import get_user_scores

# Create your views here.
def dashboard_view(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        # get score of current user in all subjects
        user_scores = get_user_scores(user_id)
        # get names of highest scorer in all subjects
        # highest_scorers = get_highest_scorer_in_all_subjects()
        context = {
            "user_scores": user_scores
        }
        # return all values to template for display
        return render(request, "home.html", context)
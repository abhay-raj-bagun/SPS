from .models import SubjectScores

# Create your views here.
def get_user_scores(user_id):
    score_details = SubjectScores.objects.filter(user_id=user_id).all()
    final_details = []
    for score_detail in score_details:
        final_details.append({
            score_detail.subject_id.subject_name : score_detail.score
        })

    return final_details


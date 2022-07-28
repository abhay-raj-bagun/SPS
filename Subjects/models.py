from django.db import models
from Users.models import User

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=30)

    class Meta:
        verbose_name    = "subject"
        db_table        = "subject"


class SubjectScores(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Users_user')
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    score = models.IntegerField()

    class Meta:
        verbose_name    = "subject_scores"
        db_table        = "subject_scores"
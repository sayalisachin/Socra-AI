# genai_webapp/models.py

from django.db import models

class UserSubmissions(models.Model):
    submission_type = models.CharField(max_length=10, choices=[('code', 'Code'), ('quiz', 'Quiz')])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.submission_type} submitted on {self.created_at}"

class AIResponses(models.Model):
    submission = models.ForeignKey(UserSubmissions, on_delete=models.CASCADE)
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Response for {self.submission.submission_type} on {self.created_at}"

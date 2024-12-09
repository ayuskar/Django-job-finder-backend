from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
#Jobs model
class Job(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
#JobApplication
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"


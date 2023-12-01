from django.db import models
from users.models import AbstractUser

class Thread(models.Model):
    author = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    gambar = models.ImageField(null=True, blank=True, upload_to='image_thread',)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class ThreadComment(models.Model):
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    ref_thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
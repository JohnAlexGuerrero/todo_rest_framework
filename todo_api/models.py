from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    task = models.CharField(("tarea"), max_length=180)
    timestamp = models.DateTimeField(("creacion"), auto_now_add=True, blank=True, auto_now=False)
    completed = models.BooleanField(("completo"), default=False, blank=True)
    updated = models.DateTimeField(("actualizacion"), auto_now=False, blank=True)
    user = models.ForeignKey(User, verbose_name=("users"), on_delete=models.CASCADE, blank=True, null=True)
    

    class Meta:
        verbose_name = ("Todo")
        verbose_name_plural = ("Todos")

    def __str__(self):
        return self.task

    # def get_absolute_url(self):
    #     return reverse("Todo_detail", kwargs={"pk": self.pk})

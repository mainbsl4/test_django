from django.db import models
from a.models import A

# Create your models here.

class B(models.Model):
    a = models.ForeignKey(A, related_name='a_db', on_delete=models.CASCADE)
    dic_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # def save(self, *args, **kwargs):
    #     # Automatically decrement book quantity upon sale
    #     self.a.value -= self.dic_value
    #     self.a.save()
    #     super().save(*args, **kwargs)
    
    # def delete(self, *args, **kwargs):
    #     # Automatically increment book quantity upon deletion
    #     self.a.value += self.dic_value
    #     self.a.save()
    #     super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.dic_value} copies of {self.a.name} on {self.created_at}"

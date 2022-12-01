from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=50);
    age = models.IntegerField();
    weight = models.FloatField();
    sex = models.CharField(max_length=20, default="Not Informed");

    group = models.ForeignKey("groups.Group", on_delete=models.CASCADE, related_name='pets');
    traits = models.ManyToManyField("traits.Trait", related_name='pets_traits'); 

from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100)
    parent_districts = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='child_districts')
    districts = models.Manager()  # this variable for District.object.all() ----> District.districts.all()
    def __str__(self):
        return self.name


class Distance(models.Model):
    source_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='source_distances')
    destination_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='destination_distances')
    distance = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.source_district} to {self.destination_district}: {self.distance} km'
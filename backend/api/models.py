from django.db import models

"""This is the model class Film"""
class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    box_office = models.IntegerField(default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'release_date': self.release_date,
            'box_office': self.box_office
        }
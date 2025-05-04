from django.db import models

class Course(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    points = models.PositiveIntegerField()

    # STATUS_CHOICES = [
    #     ('Active', 'Active'),
    #     ('Inactive', 'Inactive'),
    # ]
    # status = models.CharField(
    #     max_length=10,
    #     choices=STATUS_CHOICES,
    #     default='Active',
    # )

    def __str__(self):
        return self.title
       


from django.db import models

class Registration(models.Model):

    NEET_CHOICES = [
    ('qualified', 'Qualified'),
    ('not_qualified', 'Not Qualified'),
    ('waiting', 'Waiting for Result'),
    ('appearing', 'Appearing This Year'),
    ]


    COLLEGE_CHOICES = [
        ('govt', 'Government'),
        ('private', 'Private'),
        ('abroad', 'Abroad'),
    ]

    LOAN_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    

    fullname = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    neet_status = models.CharField(max_length=20, choices=NEET_CHOICES)
    college_preference = models.CharField(max_length=20, choices=COLLEGE_CHOICES)
    education_loan = models.CharField(max_length=5, choices=LOAN_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
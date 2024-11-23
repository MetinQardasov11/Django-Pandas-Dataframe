from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50, choices=[
        ('Mercedes', 'Mercedes'),
        ('BMW', 'BMW'),
        ('Honda', 'Honda'),
        ('Tesla', 'Tesla'),
        ('Ferrari', 'Ferrari'),
    ])
    model = models.CharField(max_length=100)
    max_speed = models.IntegerField()
    country = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f'{self.brand} {self.model}'
    
    def save(self, *args, **kwargs):
        if self.brand == 'Tesla':
            self.country = 'USA'
        elif self.brand == 'Mercedes':
            self.country = 'Germany'
        elif self.brand == 'BMW':
            self.country = 'Germany'
        elif self.brand == 'Honda':
            self.country = 'Japan'
        elif self.brand == 'Ferrari':
            self.country = 'Italy'
        super().save(*args, **kwargs)
        
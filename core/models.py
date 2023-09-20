from django.db import models

class Country(models.Model):
    COUNTRIES = [
        ('Польша', 'Польша'),
        ('Германия', 'Германия'),
        ('Литва', 'Литва'),
        ('Испания', 'Испания'),
        ('Бельгия', 'Бельгия'),
        ('Великобритания', 'Великобритания'),
    ]
    name = models.CharField(max_length=255, choices=COUNTRIES)
    tag = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    description = models.TextField()
    salary_range = models.CharField(max_length=255)
    manager_account = models.CharField(max_length=255)
    profit_type = models.CharField(max_length=255)
    profit_amount = models.FloatField()
    working_conditions = models.TextField()
    contact_person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vacancy in {self.city}, {self.country}"
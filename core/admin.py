from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from .models import Vacancy, Country, Person
from django.urls import path
from django.shortcuts import render



@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['specialization']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
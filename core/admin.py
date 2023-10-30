from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from .models import Vacancy, Country, Person, Applicant
from django.urls import path
from django.shortcuts import render



@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'specialization', 'unique_id']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Applicant)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'vacancy_id']
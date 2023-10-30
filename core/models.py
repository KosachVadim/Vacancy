from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
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
    unique_id = models.CharField(max_length=10, unique=True, default='', editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_vacancies = Vacancy.objects.filter(country=self.country)
            if existing_vacancies.exists():
                # Если есть существующие вакансии с тегами для этой страны,
                # найдем максимальный номер и увеличим его на 1
                max_unique_id = existing_vacancies.aggregate(models.Max('unique_id'))['unique_id__max']
                if max_unique_id:
                    # Используем длину текущего тега для извлечения номера
                    tag_length = len(self.country.tag)
                    unique_id_num = int(max_unique_id[tag_length:]) + 1
                else:
                    unique_id_num = 1
            else:
                # Если нет существующих вакансий для этой страны, начнем с 1
                unique_id_num = 1

            # Генерируем новый тег с учетом номера
            self.unique_id = f"{self.country.tag}{unique_id_num:04d}"

        super(Vacancy, self).save(*args, **kwargs)

    def __str__(self):
        return f"Vacancy in {self.city}, {self.country}"
class Applicant(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vacancy_id = models.IntegerField()

    def __str__(self):
        return self.name





from django.db import models


class Врач(models.Model):
    Name = models.CharField(max_length=50)
    Speciality = models.CharField(max_length=50)


class Пациент(models.Model):
    Name = models.CharField(max_length=50)
    Date_of_birth = models.DateField()
    SEX = models.CharField(max_length=10)


class Пожелания_пациентов(models.Model):
    ID_пациента = models.ForeignKey(Пациент, on_delete=models.CASCADE)
    Spciality_врача = models.CharField(max_length=50)
    Wish = models.TextField()


class Записи_пациентов_к_врачам(models.Model):
    ID_пациента = models.ForeignKey(Пациент, on_delete=models.CASCADE)
    ID_врача = models.ForeignKey(Врач, on_delete=models.CASCADE)
    DATE_записи = models.DateField()
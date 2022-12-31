from django.db import models
#from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel


# Create your models here.
class Course(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Nombre", unique=True)
    description = models.TextField(verbose_name="Descripción")
    #image = models.ImageField(verbose_name="Imagen", blank=True, null=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'photos'):
            return self.image.photos
        else:
            return "/static/images/1.jpg"

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.name


class Cohort(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Curso")
    name = models.CharField(max_length=150, verbose_name="Nombre de la Cohorte")
    initial_date = models.DateField(verbose_name="Fecha de Inicio")
    end_date = models.DateField(verbose_name="Fecha fin")
    effective_cost = models.FloatField(verbose_name="Costo en efectivo")
    credit_cost = models.FloatField(verbose_name="Costo a crédito")


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Cohorte"
        verbose_name_plural = "Cohortes"

    def __str__(self):
        return f"{self.course} {self.name}"

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=35, verbose_name="ФИО")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(unique=True,max_length=11, verbose_name="Телефон")
    company = models.CharField(max_length=100, verbose_name="Компания", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

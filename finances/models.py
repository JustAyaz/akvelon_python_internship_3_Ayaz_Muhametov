from django.db import models


class User(models.Model):
    id = models.AutoField(verbose_name='Id', primary_key=True)
    firstname = models.TextField(verbose_name='Имя', max_length=64)
    lastname = models.TextField(verbose_name='Фамилия', max_length=64)
    email = models.CharField(verbose_name='Email', max_length=100, unique=True)


class Transaction(models.Model):
    id = models.AutoField(verbose_name='Id', primary_key=True)
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name="transactions")
    amount = models.IntegerField(verbose_name='Сумма')
    date = models.DateField(verbose_name='Дата', auto_now_add=True,)
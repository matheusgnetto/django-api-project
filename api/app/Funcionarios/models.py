from django.db import models
import requests

class Funcionario(models.Model):
  name = models.CharField(max_length=255)
  salary = models.FloatField()
  age = models.IntegerField()
  role = models.CharField(max_length=255)
  email = models.EmailField()
  created_at = models.DateField(auto_now_add=True)

  @property
  def salary_brl(self):
    req = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = req.json()
    cotacao_atual = cotacao['USD']['bid']
    total = float(self.salary) * float(cotacao_atual)
    return float("{:.2f}".format(total))






from django.contrib import admin
from .models import Funcionario

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'salary_brl', 'age', 'role', 'email', 'created_at')
  
    def __str__(self):
        return "%s %s"%(self.id, self.name, self.salary, self.salary_brl, self.age, self.role, self.email, self.created_at)
  
admin.site.register(Funcionario, FuncionarioAdmin)



  

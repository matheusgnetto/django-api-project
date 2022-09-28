## ORGANIZANDO O ESPAÇO DE TRABALHO

### REQUISITOS


#### 01 - Verificar a Instalaçao do Python
```
python --version
sudo apt install python
```

#### 02 - Verificar a instalaçao do pip
```
pip --version
sudo apt-get install python-pip
```

#### 03 - Verificar instalaçao da VirtualEnv
```
sudo apt install python-virtualenv
```

### Preparando o Ambiente

#### 00 - Inicializar o Diretório com o Git Flow
```
git flow init
criar o arquivo .gitignore
```

#### 01 - Criar uma VirtualEnv
```
python -m venv "nomedavenv"
```

#### 02 - Ativar o Ambiente Virtual
```
source nomedavenv/bin/activate
```

#### 03 - Instalar as Dependencias
```
pip install django
pip install djangorestframework
```

#### 04 - Criar o Projeto
```
django-admin startproject "nomedoprojeto" .
```

#### 05 - Criar a área de administraçao e as tabelas inciais
```
python manage.py migrate
```

#### 06 - Criar o Super Usuário
```
python manage.py createsuperuser
```

#### 07 - Rodar a aplicaçao
```
python manage.py runserver
```

### Finalizando o Projeto

#### 01 - Finalizar a Feature
```
git flow feature finish "nomedafeature"
```

#### 02 - Criar a Release
```
git flow release start "numerodarelease"
```

#### 03 - Finalizar a Release
```
git flow release finish "numerodarelease"
```

#### 04 - Subir para o GitHub

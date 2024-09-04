# **Python my library (zilog-utils)**

## Contents

- [**Python my library (zilog-utils)**](#python-my-library-zilog-utils)
  - [Contents](#contents)
  - [Документация](#документация)
  - [How to install](#how-to-install)
    - [Использование команды PIP:](#использование-команды-pip)
    - [Используя Nexus](#используя-nexus)
  - [Nexus](#nexus)
 
## Документация

Пользовательскую документацию можно получить по [этой ссылке](./docs/ru/loggin.md).

## How to install

### Использование команды PIP:

    pip install zilog-logguru

### Используя Nexus

Добавить строку в requirements.txt

    zilog-logguru==0.0.1

Добавить индекс в Dockerfile

    RUN python -m pip install --upgrade pip && pip install --verbose --no-cache-dir -r requirements.txt -i https://nexus.dpd.ru/repository/pypi-all/simple

## Nexus

- .pypirc

```
[distutils]
index-servers =
    pypi
    nexus
 
[pypi]
repository:https://pypi.python.org/pypi
 
[nexus]
repository=https://nexus.dpd.ru/repository/pypi-gi/
username=sstrukov
password=<hidden>
```

- Обновить пакеты
 
```
py -m pip install --upgrade pip
py -m pip install --upgrade build
py -m pip install --upgrade twine
```

- Подправить файл setup.py, установить актуальную версию
 
- Собрать дистрибутив
  
```
py -m build
```  

- Положить дистрибутив в nexus

```
py -m twine upload --verbose -r nexus dist/*
```  

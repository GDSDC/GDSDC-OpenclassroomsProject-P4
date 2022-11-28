<h3 align="center">
    <img alt="Logo" title="#logo" width="236px" src="/assets/16007793690358_chess club-01.png">
    <br>
</h3>


# OpenClassrooms Projet P4

- [Objectif](#obj)
- [Compétences](#competences)
- [Technologies](#techs)
- [Requirements](#reqs)
- [Architecture](#architecture)
- [Configuration locale](#localconfig)
- [Présentation](#presentation)

<a id="obj"></a>
## Objectif

Le club d'échecs local nous a contacté pour développer une programme logiciel Python permettant de gérer leurs tournois de façon hors ligne et en ligne de commande.


<a id="competences"></a>
## Compétences acquises
- Utiliser la programmation orientée objet pour développer un programme Python
- Écrire un code Python robuste en utilisant la PEP 8
- Structurer le code d'un programme Python en utilisant un design pattern

<a id="techs"></a>
## Technologies Utilisées
- [Python3](https://www.python.org/)
- [Pytest](https://docs.pytest.org/)
- [Flake8](https://flake8.pycqa.org/)
- [TinyDB](https://tinydb.readthedocs.io/)

<a id="reqs"></a>
## Requirements
- flake8
- flake8-html
- pytest
- tinydb

<a id="architecture"></a>
## Architecture et répertoires
```
Project
├── core : package principale de notre application
│   ├── controller.py
│   ├── model.py
│   ├── parse_validate_tools.py
│   ├── persistence.py
│   ├── sorters.py
│   ├── vue.py
│
├── main.py : script principal destiné à lancer l'application
│
├── flake8-rapport : répertoire de résultats flake8
├── .flake8 : fichier de configuration flake8
│
├── tests : répertoire de tests
├── ressources : répertoire contenant la base de donnée initiale db.json
├── requirements.txt
```

<a id="localconfig"></a>
## Configuration locale
## Installation

### 1. Récupération du projet sur votre machine locale

Clonez le repository sur votre machine.

```bash
git clone https://github.com/GDSDC/OpenclassroomsProject-P4.git
```

Accédez au répertoire cloné.
```bash
cd OpenclassroomsProject-P4
```

### 2. Création d'un environnement virtuel 
Créez l'environnement virtuel env.
```bash
python3 -m venv env
```

### 3. Activation et installation de votre environnement virtuel 

Activez votre environnement virtuel env nouvellement créé.
```bash
source env/bin/activate
```

Installez les paquets présents dans la liste requirements.txt
```bash
pip install -r requirements.txt
```

## Utilisation

Lancer simplement le script python main.py présent à la source du dossier de travail.
```bash
python3 main.py
```



<a id="presentation"></a>
### Présentation

[<img alt="presentation" width="480px" src="/assets/presentation.png">](https://docs.google.com/presentation/d/e/2PACX-1vTsdzZ2VBaYxwU93S8pesBAk_UqTC6uP2NOe07hEvOeCCY6PFjdQcR9Jwfvac0QGqPcn13YmMNeBjWQ/pub?start=true&loop=false&delayms=5000)



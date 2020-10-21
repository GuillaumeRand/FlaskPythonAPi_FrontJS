# ProjetPrythonFlask
INSTALLATION DU PROJET

# ÉTAPE 01 : BASE DE DONNÉE

ModelisationBdd -> Modelisation de la Base de données du site Web 
Lancer le serveur MySQL, accéder au gestionnaire de base de donnée
Éxécuter le script permettant la création de la base de donnée : Step01/index.sql

# ÉTAPE 02
git clone git@github.com:EpitechIT2020/T-WEB-501-MPL-5-1-jobboard-guillaume1.rand.git
modifier le fichier Step04/app.py pour permettre la connexion à votre base de donnée 
app.config['MYSQL_DATABASE_USER'] = '.....'
app.config['MYSQL_DATABASE_PASSWORD'] = '.....'
app.config['MYSQL_DATABASE_DB'] = '......'
app.config['MYSQL_DATABASE_HOST'] = '......'
app.config['MYSQL_DATABASE_PORT'] = ..... (integer)

# ÉTAPE 03
pip3 install Flask
pip3 install flask-mysqldb
pip3 install flask-mysql 

 
# ÉTAPE 04 
Lancer le projet sur une adresse 500
python3 app.py 

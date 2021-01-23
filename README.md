# Programme d'extraction - Mode d'emploi

<<<<<<< HEAD
**Si vous avez déjà effectué les étapes 1 et 2** et que vous n’avez ni modifié ni supprimé des éléments du programme, vous pouvez commencer à l’étape 3 directement. 

## Etape 1 - Récupération du code sur votre ordinateur  

Créer un dossier cible sur la machine dans lequel le programme sera récupéré. Le nom du dossier doit de préférence être simple. Exemple : “web_scrapper”.  
Ouvrir un terminal (Cygwin par exemple).  
Utiliser la commande suivante pour aller dans le dossier cible : 

        cd 

Copier le lien vers le dépôt GitHub du projet : git@github.com:FlorianRyda/Project2_Web_Scrapping.git  
Cloner le dépôt Github en local pour pouvoir exécuter le programme sur ordinateur en tapant la commande suivante puis en la  validant dans le terminal : 

        git clone git@github.com:FlorianRyda/Project2_Web_Scrapping.git  

Le programme devrait à présent être cloné dans le dossier cible.  
Cette étape n’aura pas besoin d’être répétée tant que le dépôt cloné ne sera pas modifié ou supprimé de votre machine.  


## Etape 2 - Créer l’environnement virtuel

Utiliser la commande python --version pour vérifier que la version de Python est 3.3 ou ultérieure.  
Si ce n’est pas le cas, il faudra réinstaller Python depuis https://www.python.org/downloads/.  
A présent il faut activer l’environnement virtuel avec le commande suivante dans le terminal :  

        python -m venv env

Un dossier “env” est à présent créé dans le dossier “scrappingprogram”. Cette étape n’aura pas besoin d’être répétée tant que  le dépôt cloné ne sera pas modifié ou supprimé de votre machine.  


## Etape 3 - Activer l’environnement virtuel

Cette procédure dépend du système d’exploitation utilisé.  

### Sous MacOS/ Linux
Taper et valider dans le terminal : 

        source env/bin/activate  

### Sous Windows 
Taper et valider dans le terminal : env/Scripts/activate.bat  

### Alternative pour Windows - Sous ma version de Windows 10 cette commande ne fonctionnait pas et j’ai plutôt utilisé la  suivante :
Utiliser la commande cd pour aller dans le dossier “env”  
Taper et valider dans le terminal : 

        source ./Scripts/activate  
Utiliser la commande :

        cd ..  

Quelle que soit la commande utilisée, le nom de l’environnement apparaîtra entre parenthèses au début de chaque ligne du  terminal.  

Dans le cas présent, ce sera :(env)  

## Etape 4 - Importer les paquets

Cette étape permet d’installer tous les modules nécessaires à l’exécution du programme.  

Taper et valider dans le terminal : 

        pip install -r requirements.txt  

Taper et valider dans le terminal : 

        pip freeze  

Une liste de modules apparaît et elle devrait au moins contenir tous les modules se trouvant dans le fichier  “requirements.txt”.  

## Etape 5 - Lancer le programme

Voici l’étape la plus attendue, il est temps de lancer ce programme !  

Taper et valider dans le terminal : 

        python -m bookscrapper.  

Durant l’exécution, le dossier “result” dans le dossier “bookscrapper” va recevoir les fichiers .csv de chaque catégorie, chacun contenant les informations de chaque livre de la catégorie.  
Les fichiers image en .jpg seront également importés dans le même document.  

L’exécution du programme prend environ 30 minutes.  


=======
Si vous avez déjà effectué les étapes 1 et 2 et que vous n’avez ni modifié ni supprimé des éléments du programme, vous pouvez commencer à l’étape 3 directement. 

Etape 1 - Récupération du code sur votre ordinateur

Créer un dossier cible sur la machine dans lequel le programme sera récupéré. Le nom du dossier doit de préférence être simple. Exemple : “web_scrapper”,
Ouvrir un terminal (Cygwin par exemple),
Utiliser la commande cd pour aller dans le dossier cible
Copier le lien vers le dépôt GitHub du projet : git@github.com:FlorianRyda/Project2_Web_Scrapping.git
Cloner le dépôt Github en local pour pouvoir exécuter le programme sur ordinateur en tapant la commande suivante puis en la validant dans le terminal : 

git clone git@github.com:FlorianRyda/Project2_Web_Scrapping.git

Le programme devrait à présent être cloné dans le dossier cible. 
Cette étape n’aura pas besoin d’être répétée tant que le dépôt cloné ne sera pas modifié ou supprimé de votre machine. 


Etape 2 - Créer l’environnement virtuel

Utiliser la commande python --version pour vérifier que la version de Python est 3.3 ou ultérieure. 
Si ce n’est pas le cas, il faudra réinstaller Python depuis https://www.python.org/downloads/. 
A présent il faut activer l’environnement virtuel avec le commande suivante dans le terminal : 
python -m venv env

Un dossier “env” est à présent créé dans le dossier “scrappingprogram”. Cette étape n’aura pas besoin d’être répétée tant que le dépôt cloné ne sera pas modifié ou supprimé de votre machine. 


Etape 3 - Activer l’environnement virtuel

Cette procédure dépend du système d’exploitation utilisé.  

Sous MacOS/ Linux
Taper et valider dans le terminal : source env/bin/activate

Sous Windows 
Taper et valider dans le terminal : env/Scripts/activate.bat

Alternative pour Windows - Sous ma version de Windows 10 cette commande ne fonctionnait pas et j’ai plutôt utilisé la suivante :
Utiliser la commande cd pour aller dans le dossier “env”
Taper et valider dans le terminal : source ./Scripts/activate
Utiliser la commande : cd ..

Quelle que soit la commande utilisée, le nom de l’environnement apparaîtra entre parenthèses au début de chaque ligne du terminal.

Dans le cas présent, ce sera :(env)

Etape 4 - Importer les paquets

Cette étape permet d’installer tous les modules nécessaires à l’exécution du programme. 

Taper et valider dans le terminal : pip install -r requirements.txt
Taper et valider dans le terminal : pip freeze

Une liste de modules apparaît et elle devrait au moins contenir tous les modules se trouvant dans le fichier “requirements.txt”. 

Etape 5 - Lancer le programme

Voici l’étape la plus attendue, il est temps de lancer ce programme !

Taper et valider dans le terminal : python -m bookscrapper. 
Durant l’exécution, le dossier “result” dans le dossier “bookscrapper” va recevoir les fichiers csv de chaque catégorie, chacun contenant les informations de chaque livre de la catégorie. 
Les fichiers image en .jpg seront également importés dans le même document. 

L’exécution du programme prend environ 30 minutes. 
>>>>>>> ec5bea57857d6ac17ec1f0c52a1d19030789dd55

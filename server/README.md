# Polystar 🚀🌌🪐

Polystar est une application de navigation spatiale inspirée de Google Maps, permettant de simuler et de planifier des trajets interplanétaires en tenant compte des forces gravitationnelles. 🌍✨ Conçue avec Flask et Python, elle offre une visualisation interactive des trajectoires et des effets de slingshot gravitationnel. 🚀🔭

## Fonctionnalités 🛰️🌠🚀
- Simulation de vols interplanétaires avec prise en compte des forces gravitationnelles.
- Affichage dynamique des trajectoires des fusées et planètes. 🌎🚀
- Calcul de la meilleure route entre les planètes en optimisant la consommation de carburant. ⛽🌌
- Utilisation des effets de fronde gravitationnelle pour économiser de l'énergie. 🏹✨
- API REST permettant d'obtenir les données des planètes et des trajets calculés. 🔄🛸
## Comment?

L'application comporte deux parties: un backend Python et une application visuelle Unity. 
Les deux aplications communiquent par protocole http.
## Les Challenges rencontrés 🚀🔬🌍

Au début, nous étions partis sur l'idée de faire une application de navigation spatiale qui prendrait en compte plusieurs éléments du système solaire, notamment :  
- L'effet gravitationnel des planètes 🌎🪐  
- Les astéroïdes et autres événements cosmiques ☄️🌠  

Cependant, nous nous sommes vite rendu compte que nous n'étions pas des spécialistes en physique spatiale, et les défis liés à notre projet sont rapidement apparus.  

### Limitations techniques 🛠️🚧
1. **Complexité des astéroïdes et événements dynamiques**  
   Implémenter des variations dynamiques dans le système solaire, comme des astéroïdes, aurait été un travail colossal pour un projet en 24h. Nous avons donc dû abandonner cette idée.  

2. **Calcul des trajectoires en environnement dynamique**  
   L'un des plus grands défis a été la prise en compte du mouvement continu des planètes dans l'algorithme de trajectoire. Estimer un trajet précis dans un système en perpétuel changement s'est révélé bien plus complexe que prévu.  
## Ce dont on est fiers 🌟🚀🛸  

Nous avons réussi à créer une carte interactive du système solaire en utilisant des langages et des outils que nous ne maîtrisions pas du tout au départ. Malgré la complexité des formules physiques et des méthodes d’ingénierie, qui nous semblaient presque incompréhensibles au début, nous avons persévéré.  

Au fil du projet, nous avons appris à dompter ces outils et développé une compréhension avancée des concepts scientifiques nécessaires, jusqu’à en avoir une maîtrise presque instinctive. 💡🔭
## Installation ⚙️📥🖥️

### Prérequis 📌📝🛠️
- Python 3.x
- Flask
- NumPy
- Matplotlib (pour la visualisation optionnelle)

### Étapes d'installation 🚀🖥️⚡
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/polystar.git
   cd polystar

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt

3. Lancez le serveur Flask :
    ```bash
    python server.py

4. Accédez à l'application :
    ```bash
    http://127.0.0.1:8000
## Utilisation

L'API permet d'effectuer des requêtes pour obtenir les trajets optimaux. Par exemple :
```
    curl -X GET "http://127.0.0.1:8000/calcul>/<origin>/<destination>"
```

où origine et destination peuvent avoir les valeurs suivantes:
- Mercury
- Venus
- Earth
- Mars
- Jupiter
- Saturne
- Uranus
- Neptune


## Déploiement sur un serveur EC2 ☁️📡🚀

Assurez-vous que git et Python3 sont installés.
1. Clonez le dépôt et installez les dépendances.
2. Démarrez le serveur en arrière-plan :
```
    nohup python3 server.py > flask.log 2>&1 &
```
3. Ouvrez le port 8000 dans le pare-feu AWS. 🔑🌍
## GUI 🖥️🎮🚀

Une interface graphique a été developpée avec Unity permettant de simuler un vrai GPS spacial.
## license 📜⚖️🛠️

Ce projet est sous licence MIT. 🚀📄
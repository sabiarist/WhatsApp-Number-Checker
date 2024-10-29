<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>
<h3 align="center">WhatsApp Number Checker</h3>
<div align="center">
  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
</div>
---

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Le WhatsApp Number Checker est un script Python qui permet de vérifier si un numéro de téléphone donné est enregistré sur WhatsApp. Il utilise l'API Graph de Facebook pour effectuer cette vérification et génère un fichier CSV contenant les résultats.

## 🏁 Getting Started <a name = "getting_started"></a>

Pour utiliser le script, vous devez avoir Python installé sur votre machine ainsi que le module `requests`. Vous devez également avoir un compte développeur Facebook et générer un token d'accès valide pour utiliser l'API Graph. 

### Prerequisites

1. Python 3.x
2. Bibliothèque `requests` (installez avec `pip install requests`)
3. Un [token d'accès](https://developers.facebook.com/tools/explorer) pour l'API Graph de Facebook
4. Un fichier CSV (`phone_numbers.csv`) contenant les numéros de téléphone à vérifier, avec un numéro par ligne.

### Installing

1. Clonez le dépôt ou téléchargez le fichier script.
2. Modifiez les variables `ACCESS_TOKEN`, `VERSION`, et `PHONE_NUMBER_ID` dans le script avec vos propres informations.
3. Préparez un fichier `phone_numbers.csv` avec les numéros de téléphone.

## 🎈 Usage <a name="usage"></a>

Le script lit les numéros de téléphone à partir du fichier phone_numbers.csv, vérifie chaque numéro pour voir s'il est enregistré sur WhatsApp, et enregistre les résultats dans un fichier CSV nommé whatsapp_check_results.csv. Chaque ligne du fichier de sortie contiendra le numéro de téléphone et un booléen indiquant sa présence sur WhatsApp.


## 🚀 Deployment <a name = "deployment"></a>

Pour déployer ce script, exécutez simplement le script dans votre terminal ou votre IDE. Assurez-vous que le fichier `phone_numbers.csv` est présent dans le même répertoire que le script.


## ⛏️ Built Using <a name = "built_using"></a>

Python 3.x
requests (bibliothèque pour les requêtes HTTP)
API Graph de Facebook


## ✍️ Authors <a name = "authors"></a>

- [@sabiarist](https://github.com/sabiarist) - Initial work
- [] - Idea
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import time
import random

app = Flask(__name__)
CORS(app)  # Permet les requêtes CORS

# Fonction pour extraire les liens d'une page
def get_links(url, max_links, depth, explored_urls):
    if depth == 3 or url in explored_urls or len(explored_urls) >= max_links:
        return []

    try:
        # Ajout de https:// si le schéma n'est pas présent
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        response = requests.get(url)
        response.raise_for_status()  # Vérifier si la requête a réussi
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        # Trouver tous les liens présents sur la page
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            # Si le lien est absolu et commence par http, on l'ajoute
            if link.startswith('http'):
                links.append(link)

        # Marquer cette URL comme explorée
        explored_urls.add(url)

        # Attendre un peu avant d'envoyer la prochaine requête pour éviter le DDoS
        time.sleep(random.uniform(0.5, 1))  # Attendre 1 seconde

        # Maintenant, on explore récursivement les autres pages liées
        all_links = links.copy()

        for link in links:
            # Ne pas dépasser la profondeur et ne pas dépasser max_links
            if len(all_links) < max_links:
                all_links.extend(get_links(link, max_links, depth-1, explored_urls))
            else:
                break

        return all_links[:max_links]

    except requests.exceptions.RequestException as e:
        # Si une erreur se produit (comme une URL inaccessible), ignorer cette page
        print(f"Erreur lors de l'accès à {url}: {e}")
        return []

@app.route('/')
def index():
    return render_template('crawler.html')

@app.route('/crawler', methods=['POST'])
def crawler():
    url = request.form.get('url')
    max_links = int(request.form.get('num', 100))
    depth = int(request.form.get('depth', 1))  # Profondeur d'exploration

    # Vérification du schéma de l'URL, ajout de 'https://' si nécessaire
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    if not url:
        return jsonify({"error": "URL manquante."}), 400

    explored_urls = set()  # Ensemble pour éviter les URL en double
    links = get_links(url, max_links, depth, explored_urls)

    return jsonify({"links": links})

if __name__ == '__main__':
    app.run(debug=True)

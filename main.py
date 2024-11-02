import requests
import csv
import time
from tqdm import tqdm  # Import de tqdm pour la barre de progression

# API Config
ACCESS_TOKEN = ""
VERSION = "v21.0"
PHONE_NUMBER_ID = ""

# CSV file paths
INPUT_FILE = "phone_numbers.csv"
OUTPUT_FILE = "whatsapp_check_results.csv"

def check_whatsapp_number(phone_number):
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    params = {"id": phone_number}

    response = requests.get(url, headers=headers, params=params)
    return response.status_code == 200

def main():
    results = []

    # Read Phone numbers from CSV file
    with open(INPUT_FILE, "r") as csvfile:
        reader = csv.reader(csvfile)
        phone_numbers = list(reader)  # Chargez tous les numéros en mémoire pour les utiliser avec tqdm

    # Ajout de la barre de progression
    for row in tqdm(phone_numbers, desc="Vérification des numéros WhatsApp"):
        phone_number = row[0]
        is_on_whatsapp = check_whatsapp_number(phone_number)
        results.append([phone_number, is_on_whatsapp])

        # Break pour éviter la surcharge de l'API
        time.sleep(0.5)

    # Output results to a CSV file
    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Phone Number", "Is on WhatsApp"])
        writer.writerows(results)

    print("Vérification terminée. Résultats enregistrés dans", OUTPUT_FILE)

if __name__ == "__main__":
    main()

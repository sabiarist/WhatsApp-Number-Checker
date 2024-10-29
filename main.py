import requests
import csv
import time

# API COnfig
ACCESS_TOKEN = "EABf2OPuv6bsBO0mqhQQ24ZBeprk57i9bpQumVAtFwcvXmmEB9dqfLrGaCPVmcNOaDXIOFcTXZAvOBUxKM336ZCrnxJ7m0x3yqxZBv7ZCjNIszg86nZAKzOhgBoS63eF6HHPGZBcuygZBg0ZAY7gZC4c1kjgwb7mMFSbkBDAyWZBhUFtjK5ZAfk8OtJMjGIP0ucwAimip7b0ym0YcMZAHBD5cUEPXhK6fGTgZDZD"
VERSION = "v21.0"
PHONE_NUMBER_ID = "495617853624861"

# CSV file paths
INPUT_FILE = "phone_numbers.csv"
OUTPUT_FILE = "whatsapp_check_results.csv"


def check_whatsapp_number(phone_number):
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    params = {"id": phone_number}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return True
    else:
        return False


def main():
    results = []

    # Read Phone numbers from CSV file
    with open(INPUT_FILE, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            phone_number = row[0]
            is_on_whatsapp = check_whatsapp_number(phone_number)
            results.append([phone_number, is_on_whatsapp])

            # Break to avoid API overload
            time.sleep(1)

    # Output results to a CSV file
    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Phone Number", "Is on WhatsApp"])
        writer.writerows(results)
    print("Vérification terminée. Résultats enregistrés dans", OUTPUT_FILE)


if __name__ == "__main__":
    main()
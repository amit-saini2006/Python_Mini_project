import os
import csv
from datetime import datetime
import requests
import matplotlib.pyplot as plt


API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

CSV_FILE = 'crypto_prices.csv'

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS, timeout=10)
    return response.json()

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamps", "coin", "price"])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for coin in data:
            writer.writerow([timestamp, coin['id'], coin['current_price']])
    print("✅ data saved to csv")

def plot_garph(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['coin'] == coin_id:
                times.append(row['timestamps'])
                prices.append(row['price'])
    
    if not times:
        print(f"No data found for {coin_id}")
        return
    
    plt.figure(figsize=(10,5))
    plt.plot(times, prices, marker='o')
    plt.title(f"price trend for {coin_id.capitalize()}")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.tight_layout()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

def main():
    print("Fetching live crypto data...")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

    print("-" * 40)
    for coin in crypto_data:
        print(f"{coin['id']} - ${coin['current_price']}")
    print("-" * 40)

    choice = input("Enter the coin name to get graph: ").strip().lower()

    if choice:
        plot_garph(choice)

if __name__ == '__main__':
    main()

"""Athar Week 1: fetch and summarize live currency exchange rates."""

import os
from pathlib import Path

import requests
from dotenv import load_dotenv


API_URL = "https://v6.exchangerate-api.com/v6/latest/USD"


class ExchangeRates:
    """Store rates received from the REST API and display a summary."""

    def __init__(self, base_currency, last_update, rates):
        self.base_currency = base_currency
        self.last_update = last_update
        self.rates = rates

    def get_rate(self, currency):
        return self.rates[currency.upper()]

    def print_summary(self):
        print("=" * 45)
        print("       CURRENCY EXCHANGE RATE TRACKER")
        print("=" * 45)
        print(f"Base Currency: {self.base_currency}")
        print(f"Last Update: {self.last_update}")
        print("-" * 45)

        for currency in ("EGP", "EUR", "GBP"):
            print(f"1 {self.base_currency} = {self.get_rate(currency):.4f} {currency}")

        print("-" * 45)
        amount = 100
        converted = amount * self.get_rate("EGP")
        print(f"{amount} USD = {converted:,.2f} EGP")
        print("=" * 45)


def fetch_exchange_rates(api_key):
    """Call a public REST endpoint and turn its JSON response into an object."""
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(API_URL, headers=headers, timeout=15)
    response.raise_for_status()
    data = response.json()

    if not isinstance(data, dict):
        raise ValueError("Unexpected API response format.")
    if data.get("result") != "success":
        raise ValueError(f"API error: {data.get('error-type', 'Unknown error')}")

    try:
        return ExchangeRates(
            base_currency=data["base_code"],
            last_update=data["time_last_update_utc"],
            rates=data["conversion_rates"],
        )
    except (KeyError, TypeError) as error:
        raise ValueError("The API response is missing required fields.") from error


def main():
    project_dir = Path(__file__).resolve().parent
    load_dotenv(project_dir / ".env")
    api_key = os.getenv("EXCHANGE_RATE_API_KEY", "").strip()

    if not api_key or api_key == "your_api_key_here":
        print("Error: set EXCHANGE_RATE_API_KEY in a .env file next to main.py.")
        return 1

    try:
        exchange = fetch_exchange_rates(api_key)
        print("API Connection Successful!")
        exchange.print_summary()
        return 0
    except requests.exceptions.Timeout:
        print("Error: the API request timed out.")
    except requests.exceptions.RequestException as error:
        print(f"Network / HTTP error: {error}")
    except (ValueError, KeyError, TypeError) as error:
        print(f"Data error: {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

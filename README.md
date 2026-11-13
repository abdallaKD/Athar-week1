# Currency Exchange Rate Tracker — Athar Week 1

A small Python application that calls a public REST API, parses its JSON response, stores the exchange-rate data in an object, and prints a formatted summary.

## Features

- Fetches current USD exchange rates for EGP, EUR, and GBP using [ExchangeRate-API](https://www.exchangerate-api.com/).
- Sends an HTTP GET request with an API key loaded from `.env`.
- Parses a JSON response into a Python dictionary.
- Stores the received data in an `ExchangeRates` class.
- Prints a formatted report and a conversion example for 100 USD.
- Handles common HTTP/network and API data errors in `main.py`.

## Requirements

- Python 3.12 (recommended)
- Miniconda/Conda, or another Python environment manager
- An API key from [ExchangeRate-API](https://www.exchangerate-api.com/)

## Setup with Miniconda (Windows)

Open **Miniconda Prompt** and run:

```bash
conda create -n athar1 python=3.12 -y
conda activate athar1
cd /d D:\Athar\Week1
python -m pip install -r requirements.txt
```

If the `athar1` environment already exists, skip the `conda create` line.

Make a local `.env` file in the project folder, using `.env.example` as a template:

```text
EXCHANGE_RATE_API_KEY=your_actual_api_key
```

**Important:** Never upload `.env` or share the real API key. The `.env.example` file is safe to share.

## Run

Run the standalone Python script:

```bash
python main.py
```

Alternatively, open the notebook (if included in the submission) after installing Jupyter:

```bash
python -m pip install notebook
jupyter notebook
```

Then open `Currency_Exchange_Tracker.ipynb` and choose **Run All**.

## Expected output (illustrative)

```text
API Connection Successful!
=============================================
       CURRENCY EXCHANGE RATE TRACKER
=============================================
Base Currency: USD
Last Update: <timestamp from API>
---------------------------------------------
1 USD = <live rate> EGP
1 USD = <live rate> EUR
1 USD = <live rate> GBP
---------------------------------------------
100 USD = <calculated amount> EGP
=============================================
```

The actual rates and timestamp are returned by the API and can change.

## Project files

- `main.py` — standalone application with error handling
- `Currency_Exchange_Tracker.ipynb` — notebook version (add your existing notebook to the submission)
- `requirements.txt` — Python packages required by the script
- `.env.example` — safe API-key configuration template
- `.gitignore` — excludes secret and generated files from Git
- `README.md` — project documentation

## Week 1 concepts covered

Python classes and objects (OOP), modules/imports, JSON parsing, HTTP/REST, API authentication via `.env`, and an isolated Conda environment.

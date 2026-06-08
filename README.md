# Trading Bot on Binance Futures Testnet

Done by Junaid Ahamed

## Overview

A Python based CLI trading bot for Binance USDT Futures Testnet. This app allows users to place market and limit orders through a structured command line interface while providing input validation, logging, and error handling.

---

## Features

* Place MARKET orders on Binance Futures Testnet
* Place LIMIT orders on Binance Futures Testnet
* Supports both BUY and SELL order sides
* Command line interface using Click
* Input validation for:

  * Trading symbol
  * Order side
  * Order type
  * Quantity
  * Price for LIMIT orders
* Structured project architecture
* Detailed logging to log files
* Exception handling for:

  * Invalid user inputs
  * Binance API errors
  * Network-related failures
* Environment variable support using python-dotenv

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── .env
├── .env.example
├── README.md
│
└── test files (gitignored)
```

---

## Requirements

* Python 3.x
* python-binance
* python-dotenv
* Click
* Requests

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd trading_bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Binance Futures Testnet Setup

### Create a Testnet Account

Visit:

https://testnet.binancefuture.com

Log in and create a Binance Futures Testnet account.

### Generate API Credentials

1. Open API Management.
2. Create a new API key.
3. Save:

   * API Key
   * Secret Key

---

## Environment Variables

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

---

## Usage

### MARKET BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

### MARKET SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001
```

### LIMIT BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 50000
```

### LIMIT SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 70000
```

---

## Sample Output

### Market Order

```text
========================================
Binance Futures Trading Bot by Junaid
========================================

Order Request Summary
---------------------
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Response
--------------
Order ID: 14515231745
Status: FILLED
Executed Qty: 0.0010
Average Price: 63555.500000

Order submitted successfully
```

### Limit Order

```text
========================================
Binance Futures Trading Bot by Junaid
========================================

Order Request Summary
---------------------
Symbol: BTCUSDT
Side: BUY
Type: LIMIT
Quantity: 0.001

Order Response
--------------
Order ID: 14515246831
Status: NEW
Executed Qty: 0.0000

Order submitted successfully
```

---

## Logging

All API activity is logged to:

```text
logs/trading_bot.log
```

Logs:

* Connection events
* Order requests
* Binance API responses
* Final order details
* Validation failures
* API exceptions
* Network-related errors

Example:

```text
INFO | Market Order Requested: BTCUSDT BUY 0.001
INFO | API Response: {...}
INFO | Final Order Details: {...}
ERROR | Unsupported symbol: INVALIDUSDT
```

---

## Error Handling

### Validation Errors

Examples:

* Unsupported symbol
* Invalid order side
* Invalid quantity
* Invalid price

### Binance API Errors

Examples:

* Invalid API credentials
* Insufficient margin
* Invalid order parameters

### Network Errors

Examples:

* Connection failures
* Request timeouts
* Temporary API connectivity issues

---

## Assumptions

* User has valid Binance Futures Testnet account.
* API credentials are configured correctly in the `.env` file.
* The provided trading symbol exists on Binance Futures Testnet.
* Testnet funds are available in the account.
* Orders are submitted to the Binance Futures Testnet environment only.

---

## Deliverables Included

* Source code
* README documentation
* requirements.txt
* Log file containing:

  * Successful MARKET order
  * Successful LIMIT order
  * Error handling example

---

## Author

Junaid Ahamed
import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

client = Client(
    api_key=os.getenv("BINANCE_API_KEY"),
    api_secret=os.getenv("BINANCE_API_SECRET")
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

print(client.futures_account())
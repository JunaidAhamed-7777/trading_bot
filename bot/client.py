import os

from dotenv import load_dotenv
from binance.client import Client

from bot.logging_config import setup_logger


class BinanceFuturesClient:
    def __init__(self):
        load_dotenv()

        self.logger = setup_logger()

        self.client = Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET")
        )

        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com/fapi"
        )

        self.logger.info(
            "Connected to Binance Futures Testnet"
        )
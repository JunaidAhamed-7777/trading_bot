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
    def get_account_info(self):
        return self.client.futures_account()
    def create_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float
    ):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
    def create_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float
    ):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
    def get_order(
        self,
        symbol: str,
        order_id: int
    ):
        return self.client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )
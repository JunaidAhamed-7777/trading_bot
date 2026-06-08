from binance.exceptions import BinanceAPIException
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()
        self.logger = setup_logger()
    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        quantity = validate_quantity(quantity)

        self.logger.info(
            f"Market Order Requested: "
            f"{symbol} {side} {quantity}"
        )
        
        response = self.client.create_market_order(
            symbol=symbol,
            side=side,
            quantity=quantity
        )
        
        self.logger.info(
            f"Order created successfully: "
            f"{response['orderId']}"
        )
        return response
from binance.exceptions import BinanceAPIException
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_quantity,
    validate_price
)
from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger
from requests.exceptions import RequestException
import time

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()
        self.logger = setup_logger()

        exchange_info = self.client.get_exchange_info()

        self.valid_symbols = {
            symbol["symbol"]
            for symbol in exchange_info["symbols"]
        }
    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):
        try:
            symbol = validate_symbol(symbol, self.valid_symbols)
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
                f"API Response: {response}"
            )

            try:
                time.sleep(1)

                order_details = self.client.get_order(
                    symbol=symbol,
                    order_id=response["orderId"]
                )

                self.logger.info(
                    f"Final Order Details: {order_details}"
                )

                return order_details
            except BinanceAPIException as e:
                self.logger.warning(
                    f"Could not fetch final order details: {e}"
                )
                return response
        except BinanceAPIException as e:
            self.logger.error(f"Error occurred while placing market order: {e}")
            raise
        except RequestException as e:
            self.logger.error(
                f"Network error while communicating with Binance: {e}"
            )
            raise
    
    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):
        try:
            symbol = validate_symbol(symbol, self.valid_symbols)
            side = validate_side(side)
            quantity = validate_quantity(quantity)
            price = validate_price(price)

            self.logger.info(
                f"LIMIT order requested: "
                f"{symbol} {side} {quantity} @ {price}"
            )

            response = self.client.create_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )

            self.logger.info(
                f"API Response: {response}"
            )

            try:
                time.sleep(1)
                order_details = self.client.get_order(
                    symbol=symbol,
                    order_id=response["orderId"]
                )
                self.logger.info(
                    f"Final Order Details: {order_details}"
                )
                return order_details
            
            except BinanceAPIException as e:
                self.logger.warning(
                    f"Could not fetch final order details: {e}"
                )
                return response
        except BinanceAPIException as e:
            self.logger.error(str(e))
            raise

        except RequestException as e:
            self.logger.error(
                f"Network error while communicating with Binance: {e}"
            )
            raise
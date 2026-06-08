from bot.orders import OrderService

service = OrderService()

response = service.place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001
)

print(response)
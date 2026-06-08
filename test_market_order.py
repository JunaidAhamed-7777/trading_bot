from bot.client import BinanceFuturesClient

client = BinanceFuturesClient()

order = client.client.futures_get_order(
    symbol="BTCUSDT",
    orderId=14511146592
)

print(order)
from bot.client import BinanceFuturesClient

client = BinanceFuturesClient()

account = client.get_account_info()

print(account["totalWalletBalance"])
import click

from bot.orders import OrderService

@click.option("--quantity", required=True, type=float)
@click.option("--price", type=float)
@click.option(
    "--side",
    type=click.Choice(
        ["BUY", "SELL"],
        case_sensitive=False
    )
)
@click.option(
    "--order-type",
    type=click.Choice(
        ["MARKET", "LIMIT"],
        case_sensitive=False
    )
)
@click.option(
    "--symbol",
    required=True,
    help="Trading pair, e.g. BTCUSDT"
)
@click.command(
    help="""
        Place MARKET or LIMIT orders
        on Binance Futures Testnet.

        Example:

        python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
        """
)

def main(
    symbol,
    side,
    order_type,
    quantity,
    price
):
    try: 
        service = OrderService()
        order_type = order_type.upper()
        if order_type == "MARKET":
            response = service.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity
            )
        elif order_type == "LIMIT":
            if price is None:
                raise click.ClickException(
                    "LIMIT orders require --price"
                )
            response = service.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )
        else:
            raise click.ClickException(
                "Order type must be MARKET or LIMIT"
            )
        
        if response["status"] in ["FILLED", "NEW", "PARTIALLY_FILLED"]:
            click.echo("\nOrder Has Been Placed Successfully",fg = "green" )
        
        click.echo("\nOrder Request Summary", fg = "blue",bold = True)
        click.echo("---------------------")
        click.echo(f"Symbol: {symbol}")
        click.echo(f"Side: {side}")
        click.echo(f"Type: {order_type}")
        click.echo(f"Quantity: {quantity}")
        
        click.echo("\nOrder Response")
        click.echo("--------------")
        click.echo(f"Order ID: {response['orderId']}")
        click.echo(f"Status: {response['status']}")
        click.echo(f"Executed Qty: {response['executedQty']}")
        
        if response.get("avgPrice"):
            click.echo(
                f"Average Price: {response['avgPrice']}"
            )
    except Exception as e:
        click.echo(f"\nOrder Failed : {e}", fg = "red")
if __name__ == "__main__":
    main()
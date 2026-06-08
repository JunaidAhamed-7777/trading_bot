import click

from bot.orders import OrderService

@click.command()
@click.option("--symbol", required=True)
@click.option("--side", required=True)
@click.option("--order-type", required=True)
@click.option("--quantity", required=True, type=float)
@click.option("--price", type=float)

def main(
    symbol,
    side,
    order_type,
    quantity,
    price
):
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
        
    click.echo("\nOrder Request Summary")
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
        
if __name__ == "__main__":
    main()
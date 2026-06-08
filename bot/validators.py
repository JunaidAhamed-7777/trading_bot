VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}

def validate_symbol(symbol: str) -> str:
    symbol = symbol.upper().strip()

    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    return symbol

def validate_side(side: str) -> str:
    side = side.upper().strip()

    if side not in VALID_SIDES:
        raise ValueError(
            f"Invalid side. Must be one of {VALID_SIDES}"
        )

    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper().strip()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Invalid order type. Must be one of {VALID_ORDER_TYPES}"
        )

    return order_type

def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than zero."
        )

    return quantity

def validate_price(price: float | None) -> float:
    if price is None:
        raise ValueError(
            "Price is required for LIMIT orders."
        )

    if price <= 0:
        raise ValueError(
            "Price must be greater than zero."
        )

    return price
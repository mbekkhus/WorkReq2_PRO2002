DISCOUNT_THRESHOLD_CENTS = 5000
DISCOUNT_RATE = 0.10


class Item:
    def __init__(self, price_cents: int, quantity: int):
        self.price_cents = price_cents
        self.quantity = quantity


class Cart:
    def __init__(self, items: list[Item]):
        self.items = items


class Order:
    def __init__(
        self,
        order_id: int,
        user_email: str,
        items: list[Item],
    ):
        self.order_id = order_id
        self.user_email = user_email
        self.items = items


def calculate_discounted_total(items: list[Item]) -> int:
    total = sum(item.price_cents * item.quantity for item in items)

    if total > DISCOUNT_THRESHOLD_CENTS:
        return int(total * (1 - DISCOUNT_RATE))
    return total


def apply_discount_to_cart(cart: Cart) -> int:
    return calculate_discounted_total(cart.items)


def generate_invoice(order: Order) -> str:
    total = calculate_discounted_total(order.items)

    return (
        f"Invoice for order {order.order_id}\n"
        f"Customer: {order.user_email}\n"
        f"Total: {total} cents"
    )


if __name__ == "__main__":
    items = [Item(price_cents=3000, quantity=2)]

    cart = Cart(items)
    order = Order(
        order_id=1,
        user_email="customer@hello.com",
        items=items,
    )

print(f"Cart total: {apply_discount_to_cart(cart)} cents")
print()
print(generate_invoice(order))

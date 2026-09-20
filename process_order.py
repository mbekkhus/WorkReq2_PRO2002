VIP_DISCOUNT_RATE = 0.20
FREE_SHIPPING_DISCOUNT = 50


def calculate_total(items):
    return sum(item["price"] * item["quantity"] for item in items)


def apply_discount(total, discount_code):
    if discount_code == "VIP":
        return total * (1 - VIP_DISCOUNT_RATE)

    if discount_code == "FREESHIP":
        return total - FREE_SHIPPING_DISCOUNT

    return total


# Placeholder for future database logic.
def save_order(user_email, total):
    print(f"Order saved for {user_email}: {total}")


# Placeholder for future notification logic.
def send_order_confirmation(user_email, total):
    print(f"Email sent to {user_email}: Your order total is {total}")


def process_order(items, user_email, discount_code, notify):
    total = calculate_total(items)
    total = apply_discount(total, discount_code)

    save_order(user_email, total)

    if notify:
        send_order_confirmation(user_email, total)

    return total


if __name__ == "__main__":
    order_items = [
        {"price": 250, "quantity": 2},
        {"price": 100, "quantity": 1},
    ]

    final_total = process_order(
        items=order_items,
        user_email="customer@hello.com",
        discount_code="VIP",
        notify=True,
    )

    print(f"Final total: {final_total}")

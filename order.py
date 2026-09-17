class Order:
    def __init__(self, user_id, user_email, items):
        self.user_id = user_id
        self.user_email = user_email
        self.items = items


# Placeholder for a future database repository.
class OrderRepository:
    def __init__(self):
        self.saved_orders = []

    def save(self, order):
        order_id = len(self.saved_orders) + 1
        self.saved_orders.append(order)
        return order_id


if __name__ == "__main__":
    order = Order(
        user_id=7,
        user_email="customer@hello.com",
        items=[{"product": "Book", "quantity": 2}, {"product": "Apple", "quantity": 3}],
    )

    repository = OrderRepository()
    order_id = repository.save(order)

    print(f"Order {order_id} saved")

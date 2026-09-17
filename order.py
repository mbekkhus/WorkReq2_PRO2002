class OrderItem:
    def __init__(self, product_name: str, quantity: int):
        self.product_name = product_name
        self.quantity = quantity


class Order:
    def __init__(
        self,
        user_id: int,
        user_email: str,
        items: list[OrderItem],
    ):
        self.user_id = user_id
        self.user_email = user_email
        self.items = items


class OrderRepository:
    def save(self, order: Order) -> int:
        raise NotImplementedError("Subclasses must implement the save method")


# Simple stub used instead of a real database.
class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = []

    def save(self, order: Order) -> int:
        self.orders.append(order)
        return len(self.orders)


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def place_order(
        self,
        user_id: int,
        user_email: str,
        items: list[OrderItem],
    ) -> int:
        order = Order(user_id, user_email, items)
        return self.repository.save(order)


if __name__ == "__main__":
    repository = InMemoryOrderRepository()
    service = OrderService(repository)

    order_items = [OrderItem("Book", 2), OrderItem("Apple", 3)]

    order_id = service.place_order(
        user_id=7,
        user_email="customer@hello.com",
        items=order_items,
    )

    print(f"Order {order_id} saved")

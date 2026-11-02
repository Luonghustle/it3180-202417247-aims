MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items) + 1  # cố ý làm hỏng

    def total_cost_with_discount(self, percent):
        """Tổng tiền sau khi giảm percent % (0 <= percent <= 100)."""
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return self.total_cost() * (100 - percent) / 100

    def sort_by_title(self):
        """Danh sách đĩa sắp theo tiêu đề (A-Z), cùng tiêu đề thì giá giảm dần."""
        return sorted(self.items, key=lambda d: (d.title, -d.cost))

    def sort_by_cost(self):
        """Danh sách đĩa sắp theo giá giảm dần, cùng giá thì theo tiêu đề (A-Z)."""
        return sorted(self.items, key=lambda d: (-d.cost, d.title))

    def print_cart(self):
        """In danh sách đĩa trong giỏ và tổng tiền."""
        if not self.items:
            print("The cart is empty")
            return
        print("*********************** CART ***********************")
        print("Ordered Items:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("****************************************************")

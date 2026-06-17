# Hệ thống Thẻ thành viên Rikkei Coffee
class MemberCard:
    VOUCHER_THRESHOLD = 200000

    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = 0
        self.add_points(points)

    def add_points(self, amount):
        if isinstance(amount, int) and amount >= 0:
            self.__points += amount

    def get_points(self):
        return self.__points

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return isinstance(bill_amount, (int, float)) and bill_amount >= MemberCard.VOUCHER_THRESHOLD

card1 = MemberCard("Le Van C", 100)

card1.add_points(50)

result = MemberCard.is_eligible_for_voucher(250000)

print(f"Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.get_points()}")
print(f"Hóa đơn 250k có được tặng Voucher không? {result}")
class CoffeeOrder:
    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    def get_total_amount(self):
        return self.__total_amount

    def calculate_final_bill(self):
        return self.__total_amount * (1 + CoffeeOrder.vat_rate)

    def reset_order(self):
        self.__total_amount = 0

    @classmethod
    def update_vat_rate(cls, new_rate):
        if 0 <= new_rate <= 1:
            cls.vat_rate = new_rate


order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

order_table1.add_item(50000)
order_table2.add_item(30000)

CoffeeOrder.update_vat_rate(0.08)

print(f"Tổng tiền {order_table1.table_number} (sau VAT): {order_table1.calculate_final_bill()} VNĐ")
print(f"Tổng tiền {order_table2.table_number} (sau VAT): {order_table2.calculate_final_bill()} VNĐ")

print(f"VAT đang áp dụng cho toàn quán: {CoffeeOrder.vat_rate}")
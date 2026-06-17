class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available


menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]


def find_drink(code):
    for drink in menu:
        if drink.code == code:
            return drink
    return None


while True:
    print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
    print("1. Xem danh sách đồ uống")
    print("2. Thêm đồ uống mới")
    print("3. Cập nhật trạng thái kinh doanh")
    print("4. Thoát chương trình")
    print("==============================================")

    choice = input("Chọn chức năng (1-4): ").strip()

    match choice:
        case "1":
            print("\n--- DANH SÁCH ĐỒ UỐNG ---")
            print("Mã món | Tên món          | Giá bán | Trạng thái")
            print("-" * 50)
            for drink in menu:
                status = "Đang bán" if drink.is_available else "Ngừng bán"
                print(f"{drink.code:<6} | {drink.name:<15} | {drink.price:<7} | {status}")

        case "2":
            code = input("Nhập mã món: ").strip()
            if find_drink(code):
                print("Mã món đã tồn tại trong hệ thống!")
                continue

            name = input("Nhập tên món: ").strip()

            try:
                price = int(input("Nhập giá bán: "))
                if price <= 0:
                    print("Giá bán không hợp lệ!")
                    continue
            except:
                print("Giá bán không hợp lệ!")
                continue

            new_drink = Drink(code, name, price)
            menu.append(new_drink)
            print(f"Thành công: Đã thêm món {name} vào thực đơn!")

        case "3":
            code = input("Nhập mã món cần cập nhật: ").strip()
            drink = find_drink(code)

            if not drink:
                print("Không tìm thấy món có mã này!")
                continue

            drink.toggle_available()
            status = "Đang bán" if drink.is_available else "Ngừng bán"
            print(f"Đã cập nhật trạng thái món {code}.")
            print(f"Trạng thái hiện tại: {status}")

        case "4":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break

        case _:
            print("Chức năng không hợp lệ!")
class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    @staticmethod
    def is_valid_card_id(card_id):
        if len(card_id) != 4:
            return False
        if not card_id.startswith("RC"):
            return False
        if not card_id[2:].isdigit():
            return False
        return True

    def earn_points(self, bill_amount):
        earned = bill_amount // 10000
        self.__points += earned

        upgraded = False
        if self.__points >= 100 and self.__tier != "VIP":
            self.__tier = "VIP"
            upgraded = True

        return earned, upgraded

    def redeem_points(self, points_to_use):
        if points_to_use <= 0 or points_to_use > self.__points:
            return False, 0

        self.__points -= points_to_use
        discount = points_to_use * MemberCard.point_value_vnd
        return True, discount

    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value


cards_database = []


def find_card(card_id):
    for card in cards_database:
        if card.card_id == card_id:
            return card
    return None


while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát chương trình")

    choice = input("Chọn chức năng (1-6): ").strip()

    match choice:
        case "1":
            if not cards_database:
                print("Danh sách thẻ trống.")
            else:
                for i, card in enumerate(cards_database, 1):
                    print(f"{i}. Mã: {card.card_id} | "
                          f"Tên: {card.name:<15} | "
                          f"Điểm: {card.points:<3} | "
                          f"Hạng: {card.tier}")

        case "2":
            print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
            card_id = input("Nhập mã thẻ: ").strip()

            if not MemberCard.is_valid_card_id(card_id):
                print("Mã thẻ không hợp lệ!")
                continue

            if find_card(card_id):
                print("Mã thẻ đã tồn tại trong hệ thống!")
                continue

            name = input("Nhập tên khách hàng: ").strip()
            card = MemberCard(card_id, name)
            cards_database.append(card)

            print("Đăng ký thẻ thành viên thành công!")
            print(f"Mã thẻ: {card.card_id}")
            print(f"Tên khách hàng: {card.name}")
            print("Điểm ban đầu: 0")
            print("Hạng thẻ: Standard")

        case "3":
            print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
            card_id = input("Nhập mã thẻ: ").strip()
            card = find_card(card_id)

            if not card:
                print("Không tìm thấy thẻ!")
                continue

            bill = int(input("Nhập tổng tiền hóa đơn: "))
            earned, upgraded = card.earn_points(bill)

            print(f"Khách hàng: {card.name}")
            print(f"Hóa đơn: {bill:,} VNĐ")
            print(f"Số điểm được tích: {earned}")
            print(f"Tổng điểm hiện tại: {card.points}")

            if upgraded:
                print("Chúc mừng! Khách hàng đã được nâng hạng lên VIP.")

            print(f"Hạng thẻ hiện tại: {card.tier}")

        case "4":
            print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")

            card_id = input("Nhập mã thẻ: ").strip()
            card = find_card(card_id)

            if not card:
                print("Không tìm thấy thẻ!")
                continue

            points = int(input("Nhập số điểm muốn sử dụng: "))
            success, discount = card.redeem_points(points)

            if not success:
                print("Không thể đổi điểm!")
                print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
                print(f"Điểm hiện tại của khách: {card.points}")
            else:
                print(f"Đã trừ {points} điểm.")
                print(f"Khách hàng được giảm giá {discount:,} VNĐ vào hóa đơn!")
                print(f"Số điểm còn lại: {card.points}")
                print(f"Hạng thẻ hiện tại: {card.tier}")

        case "5":
            print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            new_value = int(input("Nhập tỷ giá mới cho 1 điểm: "))
            MemberCard.update_point_value(new_value)
            print("Cập nhật tỷ giá thành công!")
            print(f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")

        case "6":
            print("Cảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
            break

        case _:
            print("Chức năng không hợp lệ!")
shopping_bag = {}
print("[구입]")
while True:
    item = input("상품명? ")
    if item == "":
        break
    n = int(input("수량은? "))
    shopping_bag[item] = n
    print(f"장바구니에 {item} {n}개가 담겼습니다.")
    print("")
print(f"장바구니 보기: {shopping_bag}")

print("\n[검색]")
search = input("장바구니에서 확인하고자 하는 상품은? ")
print(f"{search}은(는) {shopping_bag.get(search)}개 담겨 있습니다.")
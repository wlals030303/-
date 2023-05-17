def buy(dic):
    print("[구입]")
    item = input("상품명? ")
    
    if item:
        q = int(input("수량은? "))
        dic[item] = q
        print(f'장바구니에 {item} {q}개가 담겼습니다.\n')
        return True
    else:
        print()
        return False

def show(dic):
    print(f">>> 장바구니 보기: {dic}")
    print("")

def find(dic):
    print("[검색]")
    item = input("장바구니에서 확인하고자 하는 상품은? ")

    if item in dic:
        print(f"{item}은(는) {dic[item]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {item}은(는) 없습니다.")


shopping_bag = {}

while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)
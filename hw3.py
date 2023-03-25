def get_fixed_price(rate, dc_price):
    return dc_price / ((100-rate)/100)

rate = float(input("할인율은? "))

A_dc_price = float(input("A 상품의 할인된 가격은? "))
B_dc_price = float(input("B 상품의 할인된 가격은? "))

print("A 상품의 정가는", get_fixed_price(rate,A_dc_price),"원")
print("B 상품의 정가는", get_fixed_price(rate,B_dc_price),"원")
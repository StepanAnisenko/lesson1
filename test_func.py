def get_vat(price, vat_rate):
    if price>0:
    	vat = price / 100 * vat_rate
    	price_no_vat = price - vat
    	print(price_no_vat)
    else:
    	print("wrong number")

price1 = input("Price: ")
vat_rate1 = 18
get_vat(int(price1), vat_rate1)

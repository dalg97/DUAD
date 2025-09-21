#1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y 
# muestre el precio final tomando en cuenta que:
#    1. Si el precio es menor a 100, el descuento es del 2%.
#    2. Si el precio es mayor o igual a 100, el descuento es del 10%.

product_price = int(input("Ingrese el precio del producto: "))
total_price = 0
if product_price < 100:
    total_price = product_price - (product_price * 0.02)
else:
    total_price = product_price - (product_price * 0.1)
print(f"El precio final seria: {total_price}")
products = []
while  True:
  name = input('請輸入商品名稱：')
  if name =='q':
    break
  pric = input('請輸入商品價格：') 
  products.append([name,pric])
print(products)
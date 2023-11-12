def userInput(userprod):
  i=0
  sellers = []
  for k, item in product.items():
    if userprod in item:
      i+=1
      sellers.append(k)
  if i == 0:
    print ("None of the companies sell this product.")
  if i==1:
    print (f"Only {k} sells this product.")
  if i > 1:
    sellers_rating = []
    for seller in sellers:
      sellers_rating.append(rating[seller])
    top_seller_rating = max(sellers_rating)
    top_seller = []
    top_point = []
    for k,v in rating.items():
      if v == top_seller_rating:
        top_seller.append(k)
        top_point.append(v)
        return top_seller, top_point



products_path = "products.txt"
ratings_path = "ratings.txt"

products = open(products_path)
product_line = products.readlines()
products.close()
ratings = open(ratings_path)
rating_line = ratings.readlines()
ratings.close()

product={}
rating={}

for line in product_line:
  temp = line.split("-")
  comp = temp[0]
  prod = temp[1].strip("\n").split(",")
  product[comp]=prod

for line in rating_line:
  temp1 = line.split(",")
  comp1 = temp1[0]
  rating1 = temp1[1].strip("\n").split("/")[0]
  rating[comp1] = rating1


#main
while True:
  userprod = input("Please enter the product you want to buy:")
  if userprod == "exit":
    print ("Goodbye!")
    break
  else:
    try:
      recommend, top_point= userInput(userprod)
      if len(recommend) == 1:
        print (f"We suggest you buy {userprod} from {recommend[0]} because it has the highest ranking as {top_point[0]}")
    except:
      continue

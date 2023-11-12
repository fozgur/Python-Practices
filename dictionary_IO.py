def find_top_seller(user_product):
    count = 0
    sellers = []

    for company, items in products.items():
        if user_product in items:
            count += 1
            sellers.append(company)

    if count == 0:
        print("None of the companies sell this product.")
    elif count == 1:
        print(f"Only {sellers[0]} sells this product.")
    elif count > 1:
        sellers_rating = [rating[seller] for seller in sellers]
        top_seller_rating = max(sellers_rating)

        top_sellers = [seller for seller, rate in rating.items() if rate == top_seller_rating]
        top_points = [top_seller_rating] * len(top_sellers)

        return top_sellers, top_points


products_path = "products.txt"
ratings_path = "ratings.txt"

with open(products_path) as products_file:
    product_lines = products_file.readlines()

with open(ratings_path) as ratings_file:
    rating_lines = ratings_file.readlines()

products = {}
rating = {}

for line in product_lines:
    temp = line.split("-")
    company = temp[0]
    products_list = temp[1].strip("\n").split(",")
    products[company] = products_list

for line in rating_lines:
    temp1 = line.split(",")
    company1 = temp1[0]
    rating1 = float(temp1[1].strip("\n").split("/")[0])
    rating[company1] = rating1


# Main
while True:
    user_product = input("Please enter the product you want to buy:")
    if user_product.lower() == "exit":
        print("Goodbye!")
        break
    else:
        try:
            recommended_sellers, top_points = find_top_seller(user_product)
            if recommended_sellers:
                print(f"We suggest you buy {user_product} from {recommended_sellers[0]} because it has the highest ranking as {top_points[0]}")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

import requests

def get_5_products():
    try:
        products_bytes = requests.get("https://fakestoreapi.com/products?limit=5")
        products_json = products_bytes.json()
        print(products_json)
        if products_bytes.status_code == 200:
            print("Product get sucesfully")
        else:
            print("Could'nt get products")

        return products_json
    except:
        print("Error, couldnt reach endpoint")
    

def post_product(title, price, description, image, category):
    try:
        request = requests.post('https://fakestoreapi.com/products',
            data={
               "title": title,
               "price": price,
               "description": description,
                "image":image,
                "category": category 
            }
        )
        if request.status_code == 201:
            print("Product created sucesfully")
        else:
            print("Could'nt create products")

    except:
        print("Error, couldnt reach endpoint")

def main():
    products = get_5_products()
    for product in products:
        post_product(
            product["title"],
            product["price"],
            product["description"],
            product["image"],
            product["category"]
        )


if  __name__ == "__main__":
    main()

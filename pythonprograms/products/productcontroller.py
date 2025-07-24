from product import Product
from productdao import ProductDAO
from productservice import  ProductService


def main():
    dao = ProductDAO()
    service = ProductService(dao)
    productid = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    quantity = int(input("Enter product quantity: "))
    price = int(input("Enter product price: "))

    product = Product(productid, name, category, quantity, price)
    #service.add_product(product)
    service.update_product(productid, product)
    #print("Product added successfully")
    print("Product updated")

    products = service.get_all_products()
    for product in products:
        print(product)

if __name__ == "__main__":
    main()
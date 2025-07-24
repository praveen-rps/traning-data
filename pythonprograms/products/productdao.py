import mysql.connector

from product import Product

class ProductDAO:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@1",
            database="training"
        )
        self.cursor = self.conn.cursor()

    def add_product(self, product):
        sql = "insert into product(productid,name,category,quantity,price) values (%s,%s,%s,%s,%s)"
        values = (product.productid, product.name, product.category, product.quantity, product.price)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def get_product(self, productid):
        sql = "select * from product where productid = %s"
        values = (productid,)
        self.cursor.execute(sql, values)
        product = self.cursor.fetchone()
        return product

    def get_all_products(self):
        sql = "select * from product"
        self.cursor.execute(sql)
        products = self.cursor.fetchall()
        return products

    def delete_product(self, productid):
        sql = "delete from product where productid = %s"
        values = (productid,)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return True

    def update_product(self, productid, product):
        sql = "update product set name= %s, category = %s, quantity=%s, price = %s where productid = %s"
        values = (product.name, product.category, product.quantity, product.price, productid,)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return True




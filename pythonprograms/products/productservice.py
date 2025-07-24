

class ProductService:
    def __init__(self,dao):
        self.dao = dao

    def add_product(self, product):
        #Make all the filterations or validations
        self.dao.add_product(product)
        #sending an mail for order confirmation
        return True

    def get_product(self, productid):
        return self.dao.get_product(productid)


    def get_all_products(self):
        return self.dao.get_all_products()

    def delete_product(self, productid):
        self.dao.delete_product(productid)


    def update_product(self, productid, product):
        self.dao.update_product(productid, product)


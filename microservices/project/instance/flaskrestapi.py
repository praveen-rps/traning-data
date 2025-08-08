from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

products = [
    {'id':10001, 'name':'Laptops', 'price':75000},
     {'id':10002, 'name':'Mobiles', 'price':25000},
      {'id':10003, 'name':'Chargers', 'price':500}
]


class ProductList(Resource):
    def get(self):
        return products,200
    
    def post(self):
        data = request.get_json()
        new_product = {
            'id': data['id'],
            'name':data['name'],
            'price':data['price']
        }
        products.append(new_product)
        return new_product, 201
    
class Product(Resource):
    def get(self,id):
        product = next((p for p in products if p['id'] == id), None)
        if product:
            return product,200
        else:
            return {'Mesage':'Product Not found'}, 404
    def delete(self,id):
        product = [p for p in products if p['id'] != id ]
        return {'message':f'product {id} deleted successfully'}, 200
    
    def put(self,id):
        data = request.get_json()
        product = next((p for p in products if p['id'] == id), None)
        if product:
            product['id'] = data['id']
            product['name']=data['name']
            product['price']=data['price']
            return product, 200
        return {"message":"Product Not Found"}, 404



    
    

api.add_resource(ProductList, '/products')
api.add_resource(Product ,'/products/<int:id>')

if __name__=='__main__':
    app.run(debug=True)
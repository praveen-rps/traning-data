import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  products = [
    {id:1001,name:'Laptop', price:54000},
    {id:1002,name:'Mobile', price:32000},
    {id:1003,name:'Mouse', price:500},
    {id:1004,name:'Charger', price:140},
    {id:1005,name:'ipad', price:154000},
    {id:1006,name:'Routers', price:2310},
    {id:1007,name:'Printers', price:1000},
    {id:1008,name:'Pendrives', price:900},
    {id:1009,name:'Powerbanks', price:2000}
  ];

  constructor() { }

  getProducts(){
    return this.products;
  }

  getProductById(id:number){
    return this.products.find(p => p.id == id);
  }
}

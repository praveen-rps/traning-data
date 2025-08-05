import { Component } from '@angular/core';
import { ProductService } from '../product.service';


interface Product{
  id: number;
  name:string;
  price:number;
}
@Component({
  selector: 'app-addproduct',
  templateUrl: './addproduct.component.html',
  styleUrls: ['./addproduct.component.css']
})
export class AddproductComponent {

  
  products :Product[] = [];
   product : Product = {
    id:0,
    name:'',
    price:0
   };
   constructor(private service:ProductService){

   }

   ngOnInit(){
    this.products = this.service.getProducts();
   }

   addProduct(){
    this.service.saveProduct(this.product);
    this.product = {id:0,name:'',price:0};
   }
}

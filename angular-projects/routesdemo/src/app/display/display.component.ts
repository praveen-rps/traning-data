import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-display',
  templateUrl: './display.component.html',
  styleUrls: ['./display.component.css']
})
export class DisplayComponent {

  products : any[];

  constructor(private service:ProductService, private router:Router){
    this.products = this.service.getProducts();
  }

  view(id:number){
    console.log(id)
    let product = this.products.find(p => p.id == id)
    console.log(product.name);
    this.router.navigate([`/display`, id]);
    }

}

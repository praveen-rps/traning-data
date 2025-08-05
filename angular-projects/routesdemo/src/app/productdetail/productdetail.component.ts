import { Component } from '@angular/core';
import { ProductService } from '../product.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-productdetail',
  templateUrl: './productdetail.component.html',
  styleUrls: ['./productdetail.component.css']
})
export class ProductdetailComponent {
  product : any;

  constructor(private route:ActivatedRoute, 
    private service:ProductService){
  }

  ngOnInit(){
    const pid = Number(this.route.snapshot.paramMap.get('id'));
    this.product = this.service.getProductById(pid);
  }
}

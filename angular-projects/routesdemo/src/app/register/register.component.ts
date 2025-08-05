import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

  productForm = new FormGroup({
    id: new FormControl('',[Validators.required]),
    name: new FormControl('',[Validators.required, Validators.minLength(3)]),
    price: new FormControl('',[Validators.required, Validators.min(1)])
  });

  onSubmit(){
    
  }

}

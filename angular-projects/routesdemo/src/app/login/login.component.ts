import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username :string ='';
  password : string ='';
  
  constructor(private router:Router){}

  login(){
    if(this.username === 'admin' && this.password === '12345'){
      console.log(this.username+" "+this.password)
        this.router.navigate(['/display'])
    }
    else{
      this.router.navigate(['/register'])
    }
  }


}

import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  imports: [FormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class Login {

  username = "admin";
  passwd = "admin";
  validUser = false;

  validate(){
    if (this.username === 'admin' && this.passwd === 'admin'){
      this.validUser=true;
      console.log(this.username+" "+this.passwd)
    }
    else{
      this.validUser=false;
    }
    
  }

}

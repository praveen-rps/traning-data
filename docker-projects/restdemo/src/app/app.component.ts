import { Component } from '@angular/core';
import { UserService } from './user.service';
import { User } from './user';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'restdemo';
  user : User= {
    id:0,
    name:"",
    username:"",
    email:""
  }
  error =" ";
  constructor(private service: UserService){

  }

  fetchUser():void{
    this.service.getUser(this.user.id)
    .subscribe({
     next : data => {this.user.id=data.id, this.user.name=data.name,
      this.user.username=data.username, this.user.email=data.email },
     error: err => this.error = err
    }
    );

  }


}

import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'testingdemo';

  greeting(name:string):string{
    return "Hello "+name+" Welcome to Angular Testing";
  }

  fetchUser(){
    
  }
}

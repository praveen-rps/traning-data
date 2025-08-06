import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from './User';
@Injectable({
  providedIn: 'root'
})
export class DemoService {

  private url = "https://jsonplaceholder.typicode.com/users/";


  constructor(private http:HttpClient) { }

  multiply(a:number, b:number){
    return a*b;
  }

  
  getUserById(id:number):Observable<User>{
    return this.http.get<User>(this.url+id);
  }

  
}

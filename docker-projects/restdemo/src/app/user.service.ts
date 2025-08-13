import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private url = "http://localhost:5000/users/"

  constructor(private http:HttpClient) { }

  getUser(id:number) : Observable<User>{
    return this.http.get<User>(this.url+id)
  }

  
}

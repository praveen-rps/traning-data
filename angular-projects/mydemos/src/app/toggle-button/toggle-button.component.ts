import { Component } from '@angular/core';

@Component({
  selector: 'app-toggle-button',
  templateUrl: './toggle-button.component.html',
  styleUrls: ['./toggle-button.component.css']
})
export class ToggleButtonComponent {

  isOn:boolean=false;
  names = ["Anil", "Sunil", "Suresh","Balu","Krishna"]
  status="error";
  employees =[
    {empid:1001,name:"Karan", dept:"Finance"},
    {empid:1002,name:"Kishan", dept:"Quality"},
    {empid:1003,name:"Aman", dept:"Infra"},
    {empid:1004,name:"Murali", dept:"Quality"},
    {empid:1005,name:"Niran", dept:"Operations"}
  ];

  toggle(){
    this.isOn= !this.isOn;
  }
}

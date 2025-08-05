import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { DisplayComponent } from './display/display.component';
import { AddproductComponent } from './addproduct/addproduct.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { RegisterComponent } from './register/register.component';

const routes: Routes = [
  {path:"", component:LoginComponent},
  {path:"login", component:LoginComponent},
  {path:"display", component:DisplayComponent},
  {path:"addproduct", component:AddproductComponent},
   {path:"register", component:RegisterComponent},
  {path:"**", component:PagenotfoundComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
//export { Routes };


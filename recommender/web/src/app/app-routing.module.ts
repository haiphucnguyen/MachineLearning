import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SelectUserComponent} from "./select-user/select-user.component";

const routes: Routes = [
  {
    path: '',
    component: SelectUserComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}

import { Component, OnInit } from '@angular/core';
import {HttpService} from "../core/http.service";
import {ActivatedRoute, NavigationExtras, Router} from "@angular/router";

@Component({
  selector: 'app-select-user',
  templateUrl: './select-user.component.html',
  styleUrls: ['./select-user.component.scss']
})
export class SelectUserComponent implements OnInit {

  public users: User[];

  constructor(private httpService: HttpService,
              private activatedRoute: ActivatedRoute,
              private router: Router) { }

  ngOnInit() {
    this.users = this.activatedRoute.snapshot.data.res;
    console.log(this.users);
  }

  selectUser(user: User) {
    // let navigationExtras: NavigationExtras = {
    //   queryParams: {
    //     'user': JSON.stringify(user)
    //   }
    // };
    localStorage.setItem('user', JSON.stringify(user));
    this.router.navigate([`/user/${user.user_id}`]);
  }


}

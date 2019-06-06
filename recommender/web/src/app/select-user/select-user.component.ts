import { Component, OnInit } from '@angular/core';
import {HttpService} from "../core/http.service";
import {ActivatedRoute, Router} from "@angular/router";

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

  selectUser(user_id: string) {

    console.log(user_id);
    this.router.navigate([`/user/${user_id}`]);
  }


}

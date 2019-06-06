import { Component, OnInit } from '@angular/core';
import {HttpService} from "../core/http.service";

@Component({
  selector: 'app-select-user',
  templateUrl: './select-user.component.html',
  styleUrls: ['./select-user.component.scss']
})
export class SelectUserComponent implements OnInit {

  constructor(private httpService: HttpService) { }

  ngOnInit() {
    console.log("on init");
    this.httpService.getUsers();
  }

}

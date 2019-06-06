import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private httpClient: HttpClient) { }

  getUsers(): void {
    console.log(this.httpClient);
    console.log("get user list");
    this.httpClient.get('http://localhost:5000/users').subscribe(d => {
      console.log(d);
    });
  }


}

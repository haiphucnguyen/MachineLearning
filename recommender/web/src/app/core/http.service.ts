import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private httpClient: HttpClient) { }

  getUsers(): Observable<User[]> {
    return this.httpClient.get<User[]>('/users');
  }

  loadUserPage(user_id): Observable<any> {
    // TODO[QUY]: complete this
    return this.httpClient.get(`/recommendations/${user_id}`);
  }

  loadMovie(movie_id: string): Observable<any> {
    // TODO[QUY]: complete this
    return this.httpClient.get('/users');
  }


}

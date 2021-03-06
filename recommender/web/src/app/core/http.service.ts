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

  loadRecommendMoviesForUser(user_id): Observable<any> {
    return this.httpClient.get(`/recommendations/userid=${user_id}`);
  }

  loadTrendingMovie(): Observable<TrendingMovie[]> {
    return this.httpClient.get<TrendingMovie[]>(`/trendings`);
  }

  loadFavoriteTrendingMovies(genre: string): Observable<Movie[]> {
    return this.httpClient.get<Movie[]>(`/trendings/${genre}`);
  }

  loadMovie(user_id: string, movie_id: string): Observable<Movie[]> {
    return this.httpClient.get<Movie[]>(`/recommendations/userid=${user_id}&&movieid=${movie_id}`);
  }


}

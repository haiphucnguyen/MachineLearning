import { Injectable } from '@angular/core';
import {HttpService} from "../http.service";
import {ActivatedRouteSnapshot, RouterStateSnapshot} from "@angular/router";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class MoviePageResolverService {

    constructor(private httpService: HttpService) { }

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<any> {
        const user_id = JSON.parse(localStorage.getItem('user')).user_id;
        const movie_id = route.paramMap.get('movie_id');
        console.log("In Movie page resolver", movie_id);
        return this.httpService.loadMovie(user_id, movie_id);
    }
}

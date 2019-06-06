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
        const movie_id = route.paramMap.get('movie_id');
        console.log("In Movie page resolver", movie_id);
        return this.httpService.loadMovie(movie_id);
    }
}

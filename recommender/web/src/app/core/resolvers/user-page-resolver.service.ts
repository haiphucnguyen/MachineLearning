import { Injectable } from '@angular/core';
import {HttpService} from "../http.service";
import {ActivatedRouteSnapshot, RouterStateSnapshot} from "@angular/router";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class UserPageResolverService {

   constructor(private httpService: HttpService) { }

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<any> {
      return this.httpService.loadTrendingMovie();
  }
}

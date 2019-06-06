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
      const user_id = route.paramMap.get('user_id');
      console.log("In USers page resolver", user_id);
      return this.httpService.loadUserPage(user_id);
  }
}

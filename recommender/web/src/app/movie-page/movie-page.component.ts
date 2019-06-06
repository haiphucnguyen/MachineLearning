import { Component, OnInit } from '@angular/core';
import {HttpService} from "../core/http.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-movie-page',
  templateUrl: './movie-page.component.html',
  styleUrls: ['./movie-page.component.scss']
})
export class MoviePageComponent implements OnInit {

  public watchingMovie: Movie;
  public recommendMovies: Movie[];

  constructor(private httpService: HttpService,
              private activatedRoute: ActivatedRoute,
              private router: Router) { }

  ngOnInit() {
    const users = this.activatedRoute.snapshot.data.res;
    console.log(users);
  }

  selectUser(user_id: string) {

    console.log(user_id);
    this.router.navigate([`/user/${user_id}`]);
  }

}

import { Component, OnInit } from '@angular/core';
import {HttpService} from "../core/http.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-movie-page',
  templateUrl: './movie-page.component.html',
  styleUrls: ['./movie-page.component.scss']
})
export class MoviePageComponent implements OnInit {

  public recommendMovies: Movie[] = [];

  constructor(private httpService: HttpService,
              private activatedRoute: ActivatedRoute,
              private router: Router) { }

  ngOnInit() {
    this.recommendMovies = this.activatedRoute.snapshot.data.res;
    console.log(this.recommendMovies);
  }

  selectMovie(movie_id: string) {
    this.router.navigate([`/movie/${movie_id}`]);
  }

}

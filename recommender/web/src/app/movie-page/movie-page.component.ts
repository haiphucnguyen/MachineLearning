import { Component, OnInit } from '@angular/core';
import {HttpService} from "../core/http.service";
import {ActivatedRoute, NavigationExtras, Router} from "@angular/router";

@Component({
  selector: 'app-movie-page',
  templateUrl: './movie-page.component.html',
  styleUrls: ['./movie-page.component.scss']
})
export class MoviePageComponent implements OnInit {

  public recommendMovies: Movie[] = [];
  public title = '';

  constructor(private httpService: HttpService,
              private activatedRoute: ActivatedRoute,
              private router: Router) { }

  ngOnInit() {
    this.recommendMovies = this.activatedRoute.snapshot.data.res;
    console.log(this.recommendMovies);
    this.title = this.activatedRoute.snapshot.paramMap.get('title');
    console.log(this.title);
  }

  selectMovie(movie: Movie) {
    let navigationExtras: NavigationExtras = {
      queryParams: {
        'title': movie.moviename
      }
    };
    this.router.navigate([`/movie/${movie.movieid}`, {title: movie.moviename}]);
  }

}

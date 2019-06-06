import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.scss']
})
export class UserPageComponent implements OnInit {

  // TODO[QUY] change here
  public movies: Movie[];

  constructor(private activatedRoute: ActivatedRoute,
              private router: Router) { }

  ngOnInit() {
      this.movies = this.activatedRoute.snapshot.data.res;
  }

  selectMovie(movie_id: string) {
    this.router.navigate([`movie/${movie_id}`]);
  }

}

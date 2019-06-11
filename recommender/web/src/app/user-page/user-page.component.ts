import {Component, ElementRef, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {HttpService} from "../core/http.service";

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.scss']
})
export class UserPageComponent implements OnInit {

  // TODO[QUY] change here
  public recommendMovies: Movie[];
  public trendingMovies: TrendingMovie[];
  public user: User;
  public userHobbies: any[] = [];

  constructor(private activatedRoute: ActivatedRoute,
              private router: Router,
              private httpService: HttpService) { }

  ngOnInit() {
      this.trendingMovies = this.activatedRoute.snapshot.data.res;
      this.user = JSON.parse(localStorage.getItem('user'));
      this.user.hobbies.forEach(v => {
        this.httpService.loadFavoriteTrendingMovies(v).subscribe(data => {
            let hobbie = {
              'key': v,
              'value': data
            }
            this.userHobbies.push(hobbie);
        });
      });

      // load recommend movies
      const user_id = this.activatedRoute.snapshot.paramMap.get('user_id');
      this.httpService.loadRecommendMoviesForUser(user_id).subscribe(data => {
        this.recommendMovies = data;
      });
  }

  selectMovie(movie_id: string) {
    this.router.navigate([`movie/${movie_id}`]);
  }

}

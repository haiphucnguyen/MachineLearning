import {Component, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {HttpService} from "../core/http.service";
import {ActivatedRoute, NavigationExtras, Router, RouterStateSnapshot} from "@angular/router";

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
    // this.recommendMovies = this.activatedRoute.snapshot.data.res;
    // console.log(this.recommendMovies);
    this.title = this.activatedRoute.snapshot.params['title'];

    const user_id = JSON.parse(localStorage.getItem('user')).user_id;
    const movie_id = this.activatedRoute.snapshot.params['movie_id'];
     this.httpService.loadMovie(user_id, movie_id).subscribe(data => {
       this.recommendMovies = data;
     });
  }

  onChanges(): void {
    this.activatedRoute.params.subscribe(v => {
        this.title = v.get('title');

        const user_id = JSON.parse(localStorage.getItem('user')).user_id;
        const movie_id = v.get('movie_id');
        console.log("In Movie page resolver", movie_id);
         this.httpService.loadMovie(user_id, movie_id).subscribe(data => {
           this.recommendMovies = data;
         });
    });

  }



  selectMovie(movie: Movie) {
    let navigationExtras: NavigationExtras = {
      queryParams: {
        'title': movie.moviename
      }
    };
    this.router.navigate([`/movie/${movie.movieid}`, {title: movie.moviename}]);
    this.onChanges();
  }

}

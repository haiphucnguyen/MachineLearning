import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SelectUserComponent} from "./select-user/select-user.component";
import {UsersResolverService} from "./core/resolvers/users-resolver.service";
import {UserPageComponent} from "./user-page/user-page.component";
import {UserPageResolverService} from "./core/resolvers/user-page-resolver.service";
import {MoviePageComponent} from "./movie-page/movie-page.component";
import {MoviePageResolverService} from "./core/resolvers/movie-page-resolver.service";

const routes: Routes = [
  {
    path: '',
    component: SelectUserComponent,
    resolve: {
      res: UsersResolverService
    }
  },
  {
    path: 'user/:user_id',
    component: UserPageComponent,
    resolve: {
      res: UserPageResolverService
    }
  },
  {
    path: 'movie/:movie_id',
    component: MoviePageComponent,
    resolve: {
      res: MoviePageResolverService
    }
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [UsersResolverService]
})
export class AppRoutingModule {}

interface User {
  user_id: string,
  display_name: string,
  hobbies: string[]
}

interface Movie {
  movieid: string,
  movieimg: string,
  moviename: string,
  pre_rating: number
}

interface TrendingMovie extends Movie{
  weight: number
}

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his torys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar","A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock = media.Movie("School of Rock", "Storyline",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=LqEszt5wG9I")
ratatouille = media.Movie("Ratatouille", "Storyline",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("midnight_in_paris", "Storyline",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("hunger_games", "Storyline",
                           "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg","https://www.youtube.com/watch?v=mfmrPu43DF8")
movies = [toy_story, avatar, school_of_rock, ratatouille,midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__ + media.Movie.__module__)

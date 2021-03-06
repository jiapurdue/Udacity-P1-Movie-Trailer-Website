import media
import fresh_tomatoes

# Create a list of dictionary for each movie
mlist = []
# Covert mlist into Movie class object
list_of_movies = []

# Create a movie dictionary and add the dic to a list
toy_story = {'title': "Toy Story",
             'storyline': "A cowboy doll is profoundly threatened"
             " and jealous when a new"
             " spaceman figure supplants him as top toy in a boy's room.",
             'image': "https://images-na.ssl-images-amazon.com/"
             "images/M/"
             "MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZW"
             "JkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",
             'trailer': "https://www.youtube.com/watch?v=rNk1Wi8SvNc"
             }
mlist.append(toy_story)

# Create a movie dictionary and add the dic to a list
avatar = {'title': "Avatar",
          'storyline': "A paraplegic marine dispatched to "
          "the moon Pandora "
          "on a unique mission becomes torn between following "
          "his orders and protecting the world he feels is his home.",
          'image': "https://images-na.ssl-images-amazon.com/images"
          "/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwO"
          "Dc5MTUwMw@@._V1_.jpg",
          'trailer': "https://www.youtube.com/watch?v=d1_JBMrrYw8"
          }
mlist.append(avatar)

# Create a movie dictionary and add the dic to a list
dunkirk = {'title': "Dunkirk",
           'storyline': "Allied soldiers from Belgium, the "
           "British Empire and "
           "France are surrounded by the German Army, and evacuated "
           "during a fierce battle in World War II.",
           'image': "https://images-na.ssl-images-a"
           "mazon.com/images/M/MV5BN2YyZ"
           "jQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3MWRhZjM2XkEyXkFqcGdeQX"
           "VyMDA4NzMyOA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
           'trailer': "https://www.youtube.com/watch?v=F-eMt3SrfFU"
           }
mlist.append(dunkirk)

# Create a movie dictionary and add the dic to a list
school_of_rock = {'title': "The School of Rock",
                  'storyline': "After being kicked out of a "
                  "rock band, Dewey Finn "
                  "becomes a substitute teacher of a strict "
                  "elementary private"
                  " school, only to try and turn it into a rock band.",
                  'image': "https://images-na.ssl-images-ama"
                  "zon.com/images/M/MV5BMj"
                  "EwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_.jpg",
                  'trailer': "https://www.youtube.com/watch?v=eAry-ZV_gfs"
                  }
mlist.append(school_of_rock)

# Create a movie dictionary and add the dic to a list
paddington_2 = {'title': "Paddington 2",
                'storyline': "Paddington, now happily settled "
                "with the Brown family "
                "and a popular member of the local community, "
                "picks up a series of odd "
                "jobs to buy the perfect present for his Aunt "
                "Lucy's 100th birthday, "
                "only for the gift to be stolen.",
                'image': "https://images-na.ssl-images-amazon."
                "com/images/M/MV5BMmYwNWZ"
                "lNzEtNjE4Zi00NzQ4LWI2YmUtOWZhNzZhZDYyNmVmXkEyX"
                "kFqcGdeQXVyNzYzODM3Mzg@."
                "_V1_.jpg",
                'trailer': "https://www.youtube.com/watch?v=52x5HJ9H8DM"
                }
mlist.append(paddington_2)

# Create a movie dictionary and add the dic to a list
strong = {'title': "12 Strong",
          'storyline': "12 Strong tells the story of the "
          "first Special Forces team "
          "deployed to Afghanistan after 9/11; under the leadershi"
          "p of a new captain, the team must work with an "
          "Afghan warlord to take down the Taliban.",
          'image': "https://images-na.ssl-images-amazon.com"
          "/images/M/MV5BNTEzMjk3Nzk"
          "xMV5BMl5BanBnXkFtZTgwNjY2NDczNDM@._V1_SY1000_CR0,0,674,1"
          "000_AL_.jpg",
          'trailer': "https://www.youtube.com/watch?v=-Denciie5oA"
          }
mlist.append(strong)

# Create a movie dictionary and add the dic to a list
black_panther = {'title': "Black Panther",
                 'storyline': "T'Challa, after the death "
                 "of his father, the King of "
                 "Wakanda, returns home to the isolated, "
                 "technologically"
                 " advanced African nation to succeed to "
                 "the throne and take his rightful place as king.",
                 'image': "https://images-na.ssl-images-"
                 "amazon.com/images/M/MV5BMTg1"
                 "MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_SY1000_CR0,"
                 "0,674,1000_AL_.jpg",
                 'trailer': "https://www.youtube.com/watch?v=m9PjEG_d5CI"
                 }
mlist.append(black_panther)

# Create a movie dictionary and add the dic to a list
the_dark_knight = {'title': "The Dark Knight",
                   'storyline': "When the menace known as "
                   "the Joker emerges from his mysterious "
                   "past, he wreaks havoc and chaos on the "
                   "people of Gotham,"
                   " the Dark Knight must accept one of "
                   "the greatest psycholog"
                   "ical and physical tests of his ability"
                   " to fight injustice.",
                   'image': "https://images-na.ssl-images-"
                   "amazon.com/images/M/MV5BMTMxNTMwODM0N"
                   "F5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY10"
                   "00_CR0,0,675,1000_""AL_.jpg",
                   'trailer': "https://www.youtube.com/watch?v=g8evyE9TuYk"
                   }
mlist.append(the_dark_knight)

# Create a movie dictionary and add the dic to a list
transformers = {'title': "Transformers The Last Knight",
                'storyline': "Autobots and Decepticons are "
                "at war, with humans on "
                "the sidelines. Optimus Prime is gone. The"
                " key to saving our future"
                " lies buried in the secrets of the past, "
                "in the hidden history of Transformers on Earth.",
                'image': "https://images-na.ssl-images-ama"
                "zon.com/images/M/MV5BMTk3"
                "OTI3MDk4N15BMl5BanBnXkFtZTgwNDg2ODIyMjI@._V1_.jpg",
                'trailer': "https://www.youtube.com/watch?v=yCOvcyfRPRk"
                }
mlist.append(transformers)

# call Movie class and create object for each movie in the movie list
for i in xrange(len(mlist)):
    list_of_movies.append(media.Movie(mlist[i]['title'],
                                      mlist[i]['storyline'],
                                      mlist[i]['image'],
                                      mlist[i]['trailer']))
fresh_tomatoes.open_movies_page(list_of_movies)

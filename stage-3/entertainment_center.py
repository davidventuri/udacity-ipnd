import media
import fresh_tomatoes

# Six instances of the class Movie
big_hero_6 = media.Movie(
    "Big Hero 6",
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
    "https://www.youtube.com/watch?v=z3biFxZIJOQ",
    "Briskly-paced, action-packed, and often touching. Big Hero 6's powerful "
    "storyline is an incredible motivator for kids and adults to go into "
    "computer science.",
    "http://i.imgur.com/espB8pV.png")

babadook = media.Movie(
    "The Babadook",
    "https://upload.wikimedia.org/wikipedia/en/d/d7/The-Babadook-Poster.jpg",
    "https://www.youtube.com/watch?v=k5WQZzDRVtw",
    "A descent into madness for both the characters and the audience. The "
    "Babadook had me questioning my own sanity. Can't recall any other horror "
    "quite as effective.",
    "http://i.imgur.com/cYpHynU.png")

citizenfour = media.Movie(
    "Citizenfour",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Citizenfour_poster.jpg",
    "https://www.youtube.com/watch?v=XiGwAvd5mvM",
    "Part real-life thriller, part sobering examination of 21st century civil "
    "liberties, Citizenfour transcends ideology to offer riveting, must-see "
    "cinema.",
    "http://i.imgur.com/cYpHynU.png")

nathan_for_you = media.Movie(
    "Nathan For You",
    "https://simkl.net/posters/77/777446d08175fe7f_m.jpg",
    "https://www.youtube.com/watch?v=NO8V72pDw1o",
    "Consistently funny and intelligent. A sort of absurdist, incoherent, and "
    "mundane humor that actually works. Nathan For You is just funny, "
    "bafflingly so, and accomplishes nothing else. This is a good thing.",
    "http://i.imgur.com/HCYFJht.png")

what = media.Movie(
    "what.",
    "https://s-media-cache-ak0.pinimg.com/736x/c9/3d/72/c93d729ab7fc8494706ce31dca31f0b3.jpg",
    "https://www.youtube.com/watch?v=L2rPEiWDbgo",
    "There's layer upon layer of ridiculously smart, innovative wit at work "
    "here, from a talent who's worryingly mature and self-aware for his age.",
    "http://i.imgur.com/8RHeC2D.png")

pootie_tang = media.Movie(
    "Pootie Tang",
    "http://www.joblo.com/posters/images/full/pootie-tang-poster.jpg",
    "https://www.youtube.com/watch?v=yhBExhldRXQ",
    "Pootie Tang works, in part, because it doesn't. Which is to say the "
    "movie's special success is inextricable from the moments where it "
    "blatantly fails. A modern cult classic.",
    "http://i.imgur.com/2AmVX0u.png")

movies = [big_hero_6, babadook, citizenfour, nathan_for_you, what, pootie_tang]

# Create and open the movie website .html file
fresh_tomatoes.open_movies_page(movies)

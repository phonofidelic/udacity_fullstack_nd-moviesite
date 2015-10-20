import fresh_tomatoes
import movie_class

bbs_the_documentary = movie_class.Movie(
	"BBS: The Documentary",
	2005,
	"Through eight episodes, director Jason Scott covers the 25 year history of the Dial-Up Bulletin Board System, a modem-connected computer system that let others connect to a computer over a phone line and leave messages and trade files. Containing 200 interviews, episodes mostly consist of elaborate montages of dozens of people composing a narrative.",
	"http://www.getlamp.com/order/bbsdoc.jpg",
	"https://www.youtube.com/watch?v=aqaCKyPpsBk"
	)

get_lamp = movie_class.Movie(
	"Get Lamp",
	2010,
	"With limited sound, simple graphics, and tiny amounts of computing power, the first games on home computers would hardly raise an eyebrow in the modern era of photorealism and surround sound. In a world of Quake, Half-Life and Halo, it is expected that a successful game must be loud, fast, and full of blazing life-like action. But in the early 1980s, an entire industry rose over the telling of tales, the solving of intricate puzzles and the art of writing.",
	"http://www.getlamp.com/order/package1.jpg",
	"https://www.youtube.com/watch?v=JzOPVe7Usms"
	)

decline_of = movie_class.Movie(
	"Decline of Western Civilization",
	1981,
	"Director Penelope Spheeris surveys the late-1970s Los Angeles punk scene: X, Black Flag, Fear, Germs, Catholic Discipline, Alice Bag Band.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcTBpkQB2ft4DbZMUjk4vUz3wnzb7wNu_-cAhMl1c9Ya_7KX9e7Y",
	"https://youtu.be/aiCTq_AHcqw"
	)

movies = [bbs_the_documentary, get_lamp, decline_of]
fresh_tomatoes.open_movies_page(movies)
print("is it working?")
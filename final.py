data = open("movies.csv", 'r')
lines = data.readlines()

genres = []
titles = []
stars = []

def Your_Genre(lines):
	prompt = "> "
	print "What genre would you like to see? If it is several Genres then put a | between them. Also list the genres in alphabetical order. Ex: Comedy|Crime|Drama"
	genre_answer = raw_input(prompt)

	for i in range(1,len(lines)):
		info = lines[i].rstrip().split(",")
		genre = info[2]
		title = info[1]
		if genre.lower() == genre_answer.lower():
			titles.append(title.lower())

	if len(titles) == 0:
		return "Sorry, there are no movies with the genre",genre_answer,"try again."
	else:
		print "Here are movies with that genre!"
		return titles

print Your_Genre(lines)

def Best_Movie(lines):
	prompt = "> "
	print "Would you like to see the rating for each movie?"
	yes_or_no = raw_input(prompt)

	if yes_or_no == "yes":
		for i in range(1,len(lines)):
			info = lines[i].rstrip().split(",")
			genre = info[2]
			title = info[1]
			star_rating = info[3]
			for n in range(0,len(titles)):
				if title.lower() == titles[n].lower():
					stars.append(star_rating)
		return stars
	else:
		return "Okay, have fun watching!"

print Best_Movie(lines)
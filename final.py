data = open("movies.csv", 'r')
lines = data.readlines()

genres = []
perfect_match_titles = []
related_titles = []
perfect_match_stars = []
related_stars = []

prompt = "> "
print "What genre would you like to see? If it is several Genres then put a | between them. Also list the genres in alphabetical order. Ex: Comedy|Crime|Drama"
genre_answer = raw_input(prompt)

print ""

def Your_Exact_Genre(lines):
	for i in range(1,len(lines)):
		info = lines[i].rstrip().split(",")
		genre = info[2]
		title = info[1]
		if genre.lower() == genre_answer.lower():
			perfect_match_titles.append(title.lower())

	if len(perfect_match_titles) == 0:
		return "Sorry, there are no exact movies with the genre %s" % (genre_answer)
	else:
		print "Here are movies with that exact genre!"
		return perfect_match_titles

print Your_Exact_Genre(lines)

print ""

def Related_Genre(lines):
	for i in range(1,len(lines)):
		info = lines[i].rstrip().split(",")
		genre = info[2]
		title = info[1]
		if genre_answer.lower() in genre.lower():
			if title.lower() not in perfect_match_titles:
				related_titles.append(title.lower())

	if len(related_titles) == 0:
		return "Sorry, there are no movies with the genre %s try again" % (genre_answer)
	else:
		print "Here are some movies that are partially that genre!"
		return related_titles

print Related_Genre(lines)

print ""

prompt = "> "
print "Would you like to see the rating for each movie?"
yes_or_no = raw_input(prompt)

print ""

def Best_Exact_Movies(lines):
	if len(perfect_match_titles) == 0:
		return "There are no exact genre movie ratings."
	else:
		if yes_or_no == "yes":
			for i in range(1,len(lines)):
				info = lines[i].rstrip().split(",")
				genre = info[2]
				title = info[1]
				star_rating = info[3]
				for n in range(0,len(perfect_match_titles)):
					if title.lower() == perfect_match_titles[n].lower():
						perfect_match_stars.append(star_rating)
			return perfect_match_stars
		else:
			return "Okay, have fun watching!"

print Best_Exact_Movies(lines)

print ""

def Best_Related_Genre_Movies(lines):
	if len(related_titles) == 0:
		return "There are no movie ratings with that genre at all."
	else:
		if yes_or_no == "yes":
			for i in range(1,len(lines)):
				info = lines[i].rstrip().split(",")
				genre = info[2]
				title = info[1]
				star_rating = info[3]
				for n in range(0,len(related_titles)):
					if title.lower() == related_titles[n].lower():
						related_stars.append(star_rating)
			return related_stars
		else:
			return "Okay, have fun watching!"

print Best_Related_Genre_Movies(lines)
import json
import imdb


'''
web scrape movies
then get respective details
input.txt will contains
store/watchlist of movies

input will be movie name
and similar movies will be recommended

Movie
-cast
-genre

OrderBy
- rating
- similarity

SearchBy
- genre tags
- cast (could be multiple)
- combine results
'''


def main():
	db_collection = imdb.Cinemagoer()
	res = db_collection.search_movie('hera pheri')
	movie_id = res[0].getID()
	
	ans = db_collection.get_movie(movie_id)
	for item in ans.items():
		print(item, end = '\n\n')

	'''
	0 - title
	1 - cast
	2 - genres
	12 - rating
	'''

	return


if __name__ == '__main__':
	main()
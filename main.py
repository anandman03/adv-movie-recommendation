import json
import imdb


'''
Movie

-cast
-genre
'''


def main():
	db_collection = imdb.Cinemagoer()
	res = db_collection.search_movie('hera pheri')
	movie_id = res[0].getID()
	
	ans = db_collection.get_movie(movie_id)
	for item in ans.items():
		print(item, end = '\n\n')

	return


if __name__ == '__main__':
	main()
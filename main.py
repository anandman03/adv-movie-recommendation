import imdb
import argparse
from item_struct import ItemStructure


'''
SearchBy
- genre tags
- cast (could be multiple)
- combine results
'''

def parse_args():
	'''Parse cmd args
	:returns: parser schema as dictionary
	'''
	parser = argparse.ArgumentParser()
	parser.add_argument('--name', required=True, type=str, help='Enter movie name')
	args = parser.parse_args()
	return (args.__dict__)

def get_movie_details(movie_name):
	'''Extract movie information from imdb api
	:param movie_name: Name of movie for query
	:returns: Movie details
	'''
	imdb_store = imdb.Cinemagoer()
	movie_id = imdb_store.search_movie(movie_name)[0].getID()
	movie_details = imdb_store.get_movie(movie_id)
	return movie_details

def fill_dataset():
	'''Find details for movie in dataset
	:returns: Movie dataset
	'''
	cache = []
	with open(file='input.txt') as file:
		cache = [line.rstrip('\n') for line in file]

	for index in range(len(cache)):
		movie_details = get_movie_details(cache[index])
		cache[index] = ItemStructure(movie_details)

	return cache

def main():
	'''Main run controller
	'''
	movie_name = parse_args()['name']
	movies_dataset = fill_dataset()
	movie_details = get_movie_details(movie_name)
	movie_details = ItemStructure(movie_details)

	return


if __name__ == '__main__':
	main()

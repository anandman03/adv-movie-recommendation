import imdb
import argparse
from item_struct import ItemStructure
from recommendation_engine import RecommendationEngine


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
	parser.add_argument('--weights', required=True, nargs='*', help='Enter weights(cast, genre, director, writer)')
	args = parser.parse_args()

	if len(args.__dict__['weights']) != 4:
		exit('Weights should be of length 4')

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
	args = parse_args()
	name = args['name']
	weights = args['weights']
	
	movies_dataset = fill_dataset()
	movie_details = get_movie_details(name)
	movie_details = ItemStructure(movie_details)

	engine = RecommendationEngine(movies_dataset, movie_details)
	weights = [int(weight) for weight in weights]
	result = engine.search(weights)

	result = sorted(result, reverse=True)
	for item in result:
		title = item.get_item().get_title()
		rating = item.get_item().get_rating()
		print(f'Title: {title} (Rating: {rating})')

	return


if __name__ == '__main__':
	main()

from item_struct import ItemStructure, ResultStruct


class RecommendationEngine:
	'''Recommendation Engine
	'''

	def __init__(self, dataset: list, ref_item: ItemStructure):
		'''Initialize params
		:param dataset: List of content items
		:param ref_items: Target content item
		:returns: None
		'''
		self.dataset = dataset
		self.ref_item = ref_item

	def search(self, weights: list) -> list:
		'''Search similar content in dataset
		:param weights: List of weights
		:returns: List of results
		'''
		if self.validate_weights(weights) == []:
			return []

		result = []
		for data in self.dataset:
			points = (weights[0] * self.search_by_cast(data.get_cast()))
			points += (weights[1] * self.search_by_genre(data.get_genres()))
			points += (weights[2] * self.search_by_director(data.get_director()))
			points += (weights[3] * self.search_by_writer(data.get_writer()))
			result.append(ResultStruct(points, data))

		result = self.filter_results(result)
		return result

	def filter_results(self, result: list) -> list:
		'''Filter and Sort results on points
		:param result: Result array
		:returns: List of result array
		'''
		result = filter(lambda item: item.get_points() > 0.0, result)
		result = sorted(result, reverse=True)
		return result

	def validate_weights(self, weights: list) -> list:
		'''Normalize weights
		:param weights: List of weights
		:returns: List of normalized weights
		'''
		total = sum(weights)
		weights = [(float(weight) / total) for weight in weights]
		return weights

	def search_by_writer(self, data):
		'''Search result by writer reference
		:param data: Data point from dataset
		:returns: normalized points
		'''
		writers = self.ref_item.get_writer()
		common_results = writers.intersection(data)
		return self.weighted_result(len(common_results), len(writers))

	def search_by_director(self, data):
		'''Search result by director reference
		:param data: Data point from dataset
		:returns: normalized points
		'''
		director = self.ref_item.get_director()
		common_results = director.intersection(data)
		return self.weighted_result(len(common_results), len(director))

	def search_by_genre(self, data):
		'''Search result by genre reference
		:param data: Data point from dataset
		:returns: normalized points
		'''
		genres = self.ref_item.get_genres()
		common_results = genres.intersection(data)
		return self.weighted_result(len(common_results), len(genres))

	def search_by_cast(self, data):
		'''Search result by cast reference
		:param data: Data point from dataset
		:returns: normalized points
		'''
		cast = self.ref_item.get_cast()
		common_results = cast.intersection(data)
		return self.weighted_result(len(common_results), len(cast))

	def weighted_result(self, num: int, denom: int) -> float:
		'''Calculate normalized points
		:param num: Overlapping datapoints
		:param denom: Datapoints in reference content
		:returns: normalized points
		'''
		if denom == 0:
			return 0
		return (float(num) / denom)

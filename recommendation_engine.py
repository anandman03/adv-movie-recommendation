from item_struct import ItemStructure, ResultStruct


class RecommendationEngine:
	def __init__(self, dataset: list, ref_item: ItemStructure):
		self.dataset = dataset
		self.ref_item = ref_item

	def search(self, weights: list) -> list:
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
		result = filter(lambda item: item.get_points() > 0.0, result)
		return result

	def validate_weights(self, weights: list) -> list:
		total = sum(weights)
		weights = [(float(weight) / total) for weight in weights]
		return weights

	def search_by_writer(self, data):
		writers = self.ref_item.get_writer()
		common_results = writers.intersection(data)
		return self.weighted_result(len(common_results), len(writers))

	def search_by_director(self, data):
		director = self.ref_item.get_director()
		common_results = director.intersection(data)
		return self.weighted_result(len(common_results), len(director))

	def search_by_genre(self, data):
		genres = self.ref_item.get_genres()
		common_results = genres.intersection(data)
		return self.weighted_result(len(common_results), len(genres))

	def search_by_cast(self, data):
		cast = self.ref_item.get_cast()
		common_results = cast.intersection(data)
		return self.weighted_result(len(common_results), len(cast))

	def weighted_result(self, num: int, denom: int) -> float:
		if denom == 0:
			return 0
		return (float(num) / denom)

from item_struct import ItemStructure


class ResultStruct:
	def __init__(self, points: float, ref_item: ItemStructure):
		self.points = points
		self.ref_item = ref_item

	def __lt__(self, obj):
		if self.points == obj.points:
			return (self.ref_item.get_rating() < obj.get_item().get_rating())
		return (self.points <= obj.get_points())

	def get_points(self) -> float:
		return self.points

	def get_item(self) -> ItemStructure:
		return self.ref_item


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
		return result

	def validate_weights(self, weights) -> list:
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
		return (float(num) / denom)

class ItemStructure:

	def __init__(self, item_details):
		self.title = item_details['title']
		self.cast = self.config_field(item_details['cast'])
		self.genres = set(item_details['genres'])
		self.rating = float(item_details['rating'])
		self.director = self.config_field(item_details['director'])
		self.writer = self.config_field(item_details['director'])

	def config_field(self, content):
		'''Extract names from class objects
		:param content: List of class object
		:returns: Set of extracted names
		'''
		store = []
		for element in content:
			if element.get('name') is not None:
				store.append(element.get('name'))
		return set(store)

	def get_title(self) -> str:
		return self.title

	def get_cast(self) -> set:
		return self.cast

	def get_genres(self) -> set:
		return self.genres

	def get_rating(self) -> float:
		return self.rating

	def get_director(self) -> set:
		return self.director

	def get_writer(self) -> set:
		return self.writer

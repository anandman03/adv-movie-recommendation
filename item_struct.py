class ItemStructure:

	def __init__(self, item):
		self.title = self.validate_key(item, 'title')
		self.cast = self.validate_key(item, 'cast')
		self.genres = self.validate_key(item, 'genres')
		self.rating = self.validate_key(item, 'rating')
		self.director = self.validate_key(item, 'director')
		self.writer = self.validate_key(item, 'writer')

	def validate_key(self, item, key):
		if item.get(key) is None:
			if key == 'title':
				return ''
			elif key == 'rating':
				return 0.0
			else:
				return set()

		if key == 'title':
			return item['title']
		elif key == 'rating':
			return float(item['rating'])
		elif key == 'genres':
			return set(item['genres'])
		return self.config_field(item[key])

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

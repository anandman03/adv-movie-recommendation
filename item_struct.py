class ItemStructure:
	'''Item Structure for content
	'''

	def __init__(self, item):
		'''Initialize content attributes
		:param: item: Content attributes
		:returns: None
		'''
		self.title = self.validate_key(item, 'title')
		self.cast = self.validate_key(item, 'cast')
		self.genres = self.validate_key(item, 'genres')
		self.rating = self.validate_key(item, 'rating')
		self.director = self.validate_key(item, 'director')
		self.writer = self.validate_key(item, 'writer')

	def validate_key(self, item, key):
		'''Validate attibutes in content item
		:param item: Dictionary item
		:param key: Key value
		:returns: Key value
		'''
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
		'''Get title from content item
		:returns: Title of content
		'''
		return self.title

	def get_cast(self) -> set:
		'''Get cast from content item
		:returns: Cast of content
		'''
		return self.cast

	def get_genres(self) -> set:
		'''Get genre from content item
		:returns: Genre of content
		'''
		return self.genres

	def get_rating(self) -> float:
		'''Get rating from content item
		:returns: Rating of content
		'''
		return self.rating

	def get_director(self) -> set:
		'''Get director from content item
		:returns: Director of content
		'''
		return self.director

	def get_writer(self) -> set:
		'''Get writer from content item
		:returns: Writer of content
		'''
		return self.writer


class ResultStruct:
	'''Result Structure for content
	'''

	def __init__(self, points: float, ref_item: ItemStructure):
		'''Initialize params
		:param: points: Similarity points
		:param ref_item: Content item
		:returns: None
		'''
		self.points = points
		self.ref_item = ref_item

	def __lt__(self, obj):
		'''Comparator Overloading
		:param obj: ResultStruct object for comparison
		:returns: bool comparison value
		'''
		if self.points == obj.points:
			return (self.ref_item.get_rating() < obj.get_item().get_rating())
		return (self.points <= obj.get_points())

	def get_points(self) -> float:
		'''Get points
		:returns: Similarity points
		'''
		return self.points

	def get_item(self) -> ItemStructure:
		'''Get Content item
		:returns: Content item
		'''
		return self.ref_item

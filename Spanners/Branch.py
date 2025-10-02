class Branch:
	'''
	utility to recurse down into a parsed dataframe
	'''

	def __init__(self, dq=None, stack=None):
		'''
		class object used to create isolation between levels
		and copies the dataframe into a reduced set to remove global sharing issues
		'''
		self.dq = dq.copy()
		if stack:
			self.stack = stack
		else:
			self.stack = [ OrderedDict([]) ]

	def pushd(self, value):
		self.putd(value)
		self.stack.append(
			self.stack[-1][value][-1]
		)

	def putd(self, value):
		if value not in self.stack[-1].keys():
			self.stack[-1][value] = [ OrderedDict([]) ]

	def popd(self):
		self.stack.pop()

	def graft(self, indent=''):
		columns = deque(self.dq.columns)
		if len(columns) == 0: return
		column = columns.popleft()

		for value in self.dq[column].unique():
			print(f'{indent}{value}')

			self.pushd(value)

			dqq = self.dq[self.dq[column] == value][columns]
			Branch(dq=dqq, stack=self.stack).graft(indent=f'\t{indent}')

			self.popd()

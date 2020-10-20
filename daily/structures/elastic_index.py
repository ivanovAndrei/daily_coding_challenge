import re
import string

class SearchIndex():
    def __init__(self):
        self._docs = dict()
        self._inputs = dict()

    @property
    def original_documents(self):
        return self._inputs

    def add(self, id:int, input:str):
        if id not in self._inputs.keys():
            self._inputs[id] = input

        input = re.sub('^[a-zA-Z0-9]', ' ', input)
        groups = input.split()

        for g in groups:
            frequency = input.count(g)
            if g in self._docs.keys() and not any([n for n in self._docs[g] if n[0] == id]):
                self._docs[g].append((id, frequency))
            else:
                self._docs[g] = [(id, frequency)]

    def print_data(self):
        print(self._docs)

    def search(self, input:str)->list:
        """
        :param str input: Input search string
        :rtype: list
        :returns list of document indices
        """
        return_list = []
        if input in self._docs.keys():
            return_list = self._docs[input]
        return return_list


index = SearchIndex()
index.add(0, "some more examples")
index.add(1, "Examples are great for examples of examples")
indices = index.search("examples")
print(indices)
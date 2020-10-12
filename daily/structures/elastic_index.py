import re
import string

class ElasticIndex():
    def __init__(self):
        self._freq = dict()
        self._docs = dict()

    def add_terms(self, input:str, input_id:int):
        translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
        input = input.translate(translator)
        groups = input.split()

        for g in groups:
            if g in self._freq.keys():
                self._freq[g] = self._freq[g]+1
                self._docs[g].append(input_id)
            else:
                self._freq[g] = 1
                self._docs[g] = [input_id]

    def print_data(self):
        print(self._freq)
        print(self._docs)

    def find_string(self, input:str)->int:
        if input in self._freq.keys():
            print(f"Found string {input} {self._freq[input]} times in these docs: {self._docs[input]}")



index = ElasticIndex()
index.add_terms("Mary had a little lamb", 1)
index.add_terms("Trex had tiny arms", 2)
index.add_terms("Mary the vecociraptor had long arms she could rip lambs to pieces with", 3)
index.print_data()
index.find_string("had")
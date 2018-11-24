"""
This problem was asked by Twitter.
Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

from utils import pretty_dict

class Trie:
    def __init__(self):
        self.store = {}


    def add(self, string):
        d = self.store
        i = 0
        while i < len(string):
            c = string[i]
            if not d.get(c):
                d[c] = {}
            d = d.get(c)
            i += 1
        d[" "] = string


    def __str__(self):
        return pretty_dict(self.store)


def autocomplete(d, prefix):
    if prefix == "":
        results = []
        for key in d:
            if key == " ":
                results.append(d.get(key))
            else:
                results += autocomplete(d.get(key), prefix)
        return results
    elif not d.get(prefix[0]):
        return []
    else:
        return autocomplete(d.get(prefix[0]), prefix[1:])


if __name__ == '__main__':
    trie = Trie()

    data = ["dog", "deer", "deal"]
    for word in data:
        trie.add(word)

    prefix = input("String : ")

    print(autocomplete(trie.store, prefix))
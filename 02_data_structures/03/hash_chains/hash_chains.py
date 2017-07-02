# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count

        self.elems = []
        for i in range(bucket_count):
            self.elems.append([])

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def find_el(self, idx, query):
        for el in self.elems[idx]:
            if el == query:
                return True

        return False

    def process_query(self, query):

        #print(self.elems)

        if query.type == "check":
            self.write_chain(self.elems[query.ind])
        else:
            try:
                ind = self._hash_func(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(self.find_el(ind, query.s))

            elif query.type == 'add':
                #print('add',  self.find_el(ind, query.s))
                if self.find_el(ind, query.s) == False:
                    self.elems[ind].insert(0, query.s)
            else:
                if ind != -1:
                    try:
                        self.elems[ind].remove(query.s)
                    except:
                        pass

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

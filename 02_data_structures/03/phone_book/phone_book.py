# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

phone_book = {}

def process_queries(queries):

    for cur_query in queries:

        if cur_query.type == 'add':
            phone_book[cur_query.number] = cur_query.name

        if cur_query.type == 'del':
            if phone_book.get(cur_query.number):
                del phone_book[cur_query.number]

        if cur_query.type == 'find':
            print(phone_book.get(cur_query.number, 'not found'))


if __name__ == '__main__':
    process_queries(read_queries())

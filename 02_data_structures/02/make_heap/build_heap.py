# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):

    def parent(i):
        if i > 0:
            return (i-1) // 2
        else:
            return 0

    def left_child(i):
        return 2*i + 1

    def right_child(i):
        return 2*i + 2


    size = len(self._data) - 1


    def sift_up(i):
        while i > 0 and self._data[parent(i)] > self._data[i]:
            self._swaps.append( [parent(i) , i] )
            self._data[parent(i)], self._data[i] = self._data[i], self._data[parent(i)]
            i = parent(i)

    def sift_dawn(i):
        max_index = i

        l = left_child(i)

        if l <= size and self._data[l] < self._data[max_index]:
            max_index = l

        r = right_child(i)

        if r <= size and self._data[r] < self._data[max_index]:
            max_index = r

        if i != max_index:
            self._data[i], self._data[max_index] = self._data[max_index], self._data[i]
            self._swaps.append((i, max_index))
            sift_dawn(max_index)

    for i in range(size//2, -1, -1):
        sift_dawn(i)


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

# python3
import sys

def sort_characters(string):
    n = len(string)
    return sorted(range(n), key=lambda x: string[x])

def sort_doubled(string, l, order, cl):
    n = len(string)
    
    count = [0] * n
    new_order = [0] * n
    
    for i in range(0, n):
        count[cl[i]] = count[cl[i]] + 1
    
    for j in range(1, n):
        count[j] = count[j] + count[j-1]
        
    for i in range(n-1, -1, -1):
        start = (order[i] - l + n) % n
        c = cl[start]
        count[c] = count[c] - 1
        new_order[count[c]] = start
    
    return new_order
    
def compute_char_classes(string, order):
    n = len(string)
    
    c = [0] * n
    
    c[order[0]] = 0
    
    for i in range(1, n):
        if string[order[i]] != string[order[i-1]]:
            c[order[i]] = c[order[i-1]] + 1
        else:
            c[order[i]] = c[order[i-1]]
    
    return c
    
    
def update_classes(order, cl, l):
    n = len(order)
    new_class = [0] * n
    
    new_class[order[0]] = 0
    
    for i in range(1, n):
        cur = order[i]
        prev = order[i-1]
        mid = cur + l
        mid_prev = (prev + l) % n
        
        if cl[cur] != cl[prev] or cl[mid] != cl[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]
            
    return new_class

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  
  # print(text)
  
  order = sort_characters(text)
  # print(order)
  
  cl = compute_char_classes(text, order)
  # print(cl)
  
  l = 1
  
  n = len(text)
  
  while l < n:
      order = sort_doubled(text, l, order, cl)
      cl = update_classes(order, cl, l)
      l = 2*l
  
  
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))

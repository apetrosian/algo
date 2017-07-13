# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  
  if len(text) < len(pattern):
      return []

  if text == pattern:
      return [0]
  
  result = []
  
  s = pattern + '$' + text
  
  n = len(s)
  p = len(pattern)
  
  borders = [0] * n
  b = 0
  
  for i in range(1, n):
    while b > 0 and s[i] != s[b]:
      b = borders[b-1]


    if s[i] == s[b]:
      b += 1
    else:
      b = 0
      
    if b == p:
        result.append( i - 2*p )

    borders[i] = b

  # print(s)
  # print(borders)
  
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))


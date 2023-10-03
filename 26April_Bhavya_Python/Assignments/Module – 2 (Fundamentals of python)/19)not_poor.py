# Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string. 

def not_bad(s):
  snot = s.find('not')
  sbad = s.find('bad')

  if sbad > snot:
    s = s.replace(s[snot:(sbad+3)], 'good')

  return s

print(not_bad('The lyrics is not that poor!'))
print(not_bad('The lyrics is poor!'))
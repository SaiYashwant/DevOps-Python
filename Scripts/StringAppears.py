#Program to count the number of times each word appears in a string and save it in a dictionary:

def count_Words(string):
  words = string.split()
  Word_Count = {}
  for word in words:
    word = word.lower()
    if word in Word_Count:
      Word_Count[word] += 1
    else:
      Word_Count[word] = 1
  return Word_Count

# Example usage
text = "Hello world! Hello everyone."
print(count_Words(text))

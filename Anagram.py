
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

word1 = word1.lower().replace(" ", "")
word2 = word2.lower().replace(" ", "")

if sorted(word1) == sorted(word2):
    print("Words are Anagrams")
else:
    print("Words are Not Anagrams")

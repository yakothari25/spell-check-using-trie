  

    Name: Yogesh KOthari
    Dpet: Computer Science and Engineering (Shift I)
    Desgin and Analysis of Algorithm Assignment
    Roll no: 80


# spell-check-using-trie
Spell checking using tries by python.

**Aim: Implement tries using python and demonstrate application of tries in spell checking.**

  Trie is an efficient information reTrieval data structure. Using Trie, search complexities can be brought to optimal limit (key length). If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. Using Trie, we can search the key in O(M) time.

  With Trie, we can insert and find strings in O(L) time where L represent the length of a single word. This is obviously faster than BST. This is also faster than Hashing because of the ways it is implemented. We do not need to compute any hash function. No collision handling is required (like we do in open addressing and separate chaining)

Each Node of trie data stucture contains

    1. Value
    2. Childrens: array of type Node
    3. isComplete: Boolean value to represent the word completion

This program has total 235878 words in super.file as an object of Node class.

To run make sure super.file and trie.py are in same folder

**For Spell check a word or words in sentence**
  1. Hit on "Check String"
  2. Enter String
      Note: Keep space between 2 words
  3. Hit "Check"
  4. Result will be displayed
  5. Hit "Clear" to clear entered string

**For Adding new words from text file**
  1. remove the comment(#) from addwordsdatabase()
  2. Add new words in word.txt
  3. run program
  4. hit the "Save Updates" on the menu
  
**For adding a single word**
  1. hit the "Add words" on the menu
  2. Enter words
  3. hit Add word



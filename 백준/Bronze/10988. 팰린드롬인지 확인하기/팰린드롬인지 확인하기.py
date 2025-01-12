### 240112 : palindrome
word = input().strip()
word_list = list(word)  
reversed_list = list(word)  
reversed_list.reverse()  

if word_list == reversed_list:
    print(1)
else:
    print(0)
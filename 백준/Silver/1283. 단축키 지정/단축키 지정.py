import sys
input = sys.stdin.readline

N = int(input())                 
shortcuts = set()                # 단축키 저장된 셋

for _ in range(N):
    text = input().rstrip()      
    words = text.split()       
    found = False                # 단축키 찾았니?

    # 각 단어의 첫 글자를 왼쪽부터 확인
    for i, word in enumerate(words):
        first_char = word[0].upper()  # 대소문자 구분 없으므로 대문자로 통일
        if first_char not in shortcuts:
            shortcuts.add(first_char)

            for j in range(i):
                print(words[j], end= ' ')
            print(f"[{word[0]}]{word[1:]}", end='')

            for j in range(i+1, len(words)):
                print(f" {words[j]}", end='')
            found = True
            break

    # 모든 첫 글자가 이미 지정된 경우 모든 글자 다 확인해야 함
    if not found:
        for i, word in enumerate(words):
            found_in_word = False    # 현재 단어에서 단축키 있니?
            
            # 단어의 모든 글자 확인
            for j, char in enumerate(word):
                up_char = char.upper()
                if up_char not in shortcuts:
                    shortcuts.add(up_char)
                    
                    # 현재 단어 앞까지는 그대로
                    for k in range(i):
                        print(words[k], end=' ')
                    print(f"{word[:j]}[{word[j]}]{word[j+1:]}", end='')
                    # 그 외의 단어들!!
                    for k in range(i+1, len(words)):
                        print(f" {words[k]}", end='')
                    found = True
                    found_in_word = True
                    break
            
            if found_in_word:
                break
            
            # 단축키 지정 못한 경우 원래 단어 그대로 출력
            if not found and i == len(words)-1:
                print(" ".join(words), end='')
    print()
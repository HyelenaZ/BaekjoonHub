# [Bronze V] A-B - 1001 

[문제 링크](https://www.acmicpc.net/problem/1001) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 사칙연산, 수학

### 제출 일자

2025년 1월 16일 23:39:53

### 문제 설명

<p>두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)</p>

### 출력 

 <p>첫째 줄에 A-B를 출력한다.</p>

------------------------------------------------------------------------------------
Hyo's Memo
------------------------------------------------------------------------------------
🎯 BJ 1001: A-B with 입력값 검증
# A-B 문제 분석 (입력값 검증 포함)

## 👀 출제자의 의도 분석
1. **예외 처리의 이해**
   ```python
   try:
       # 실행 코드
   except ValueError:
       # 예외 처리
   ```
   - 예외 상황 대응 능력
   - 안정적인 프로그램 작성법

2. **입력값 검증**
   ```python
   if 0 < a < 10 and 0 < b < 10:
       # 유효한 입력 처리
   ```
   - 범위 체크의 중요성
   - 복합 조건문 활용

## 📚 관련 공식 문서
1. **Python Exceptions**
   - [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
   - ValueError
   - Exception Handling

2. **Python Input Processing**
   - [input()](https://docs.python.org/3/library/functions.html#input)
   - [str.strip()](https://docs.python.org/3/library/stdtypes.html#str.strip)
   - [str.split()](https://docs.python.org/3/library/stdtypes.html#str.split)

## 💡 핵심 개념
1. **예외 처리 패턴**
   - try-except 구문
   - 구체적 예외 처리
   - 사용자 피드백

2. **입력 데이터 처리**
   - 공백 제거 (strip)
   - 문자열 분리 (split)
   - 타입 변환 (map)

3. **반복 제어**
   - while True
   - break 조건
   - 조건부 실행

## ⭐ 중요 포인트
1. **안정성**
   ```python
   # 1. 입력값 정제
   input().strip().split()
   
   # 2. 타입 변환 및 예외 처리
   try:
       map(int, ...)
   except ValueError:
       # 처리
   
   # 3. 범위 검증
   if 0 < a < 10 and 0 < b < 10:
       # 처리
   ```

⏱️ 시간 복잡도
- 입력 처리: O(1)
- 검증 과정: O(1)
- 전체: O(1)

💫 공간 복잡도
- 변수 공간: O(1)
- 전체: O(1)

⚠️ 주의사항
- 정수 입력 검증
- 범위 조건 확인
- 적절한 에러 메시지

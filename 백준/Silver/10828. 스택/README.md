# [Silver IV] 스택 - 10828 

[문제 링크](https://www.acmicpc.net/problem/10828) 

### 성능 요약

메모리: 33432 KB, 시간: 40 ms

### 분류

자료 구조, 구현, 스택

### 제출 일자

2025년 1월 18일 23:52:42

### 문제 설명

<p>정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.</p>

<p>명령은 총 다섯 가지이다.</p>

<ul>
	<li>push X: 정수 X를 스택에 넣는 연산이다.</li>
	<li>pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>size: 스택에 들어있는 정수의 개수를 출력한다.</li>
	<li>empty: 스택이 비어있으면 1, 아니면 0을 출력한다.</li>
	<li>top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
</ul>

### 입력 

 <p>첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.</p>

### 출력 

 <p>출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.</p>
 
-------------------------------------------------------------------------------------------------------
# Hyo's Memo 📚

## 📍 Stack (스택) 연산 상세
> 기본적인 스택 연산의 구현 방법과 특징 정리

### 기본 구현 🛠
```python
# Python
stack = []  # 리스트로 스택 구현
```

```java
// Java
Stack<Integer> stack = new Stack<>();
```

### 연산별 구현 방법 ⚡
#### Python 🐍
| 연산 | 구현 | 시간복잡도 |
|------|------|------------|
| push | `stack.append(x)` | O(1) |
| pop | `stack.pop()` | O(1) |
| top | `stack[-1]` | O(1) |
| empty | `len(stack) == 0` | O(1) |
| size | `len(stack)` | O(1) |

#### Java ☕
| 연산 | 구현 | 시간복잡도 |
|------|------|------------|
| push | `stack.push(x)` | O(1) |
| pop | `stack.pop()` | O(1) |
| top | `stack.peek()` | O(1) |
| empty | `stack.isEmpty()` | O(1) |
| size | `stack.size()` | O(1) |

### 입력 처리 최적화 💡
#### Python
```python
# 기본 입력
input()  # 한 줄 읽기

# 최적화된 입력
import sys
input = sys.stdin.readline  # 더 빠른 입력
command = input().strip()   # 개행문자 제거
```

#### Java
```java
// 기본 입력
Scanner sc = new Scanner(System.in);

// 최적화된 입력
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String command = br.readLine();
```

### 주의사항 ⚠️
- ✅ 빈 스택 처리 필수
- ⚠️ IndexError/EmptyStackException 주의
- 💡 입력 최적화 고려

## 📍 입출력 최적화
### Python
- `sys.stdin.readline()`: 더 빠른 입력
- `strip()`: 개행문자 제거
- `split()`: 문자열 분리

### Java
- `BufferedReader`: 버퍼 사용으로 빠른 입력
- `StringTokenizer`: 문자열 분리
- `StringBuilder`: 문자열 연산 최적화

## 📍 복잡도 분석

### 시간 복잡도 ⏱️
- 스택 기본 연산: 모두 O(1)
  - push: O(1)
  - pop: O(1) 
  - top: O(1)
  - empty: O(1)
  - size: O(1)
- 전체 프로그램: O(N)
  - N개의 명령을 각각 O(1)에 처리
  - N은 입력으로 주어지는 명령의 수 (1 ≤ N ≤ 10,000)

### 공간 복잡도 💾
- 스택 저장공간: O(N)
  - 최악의 경우 N개의 push 명령
  - 각 원소는 정수값 (1 ≤ X ≤ 100,000)
- 추가 변수: O(1)
  - 명령어 처리를 위한 임시 변수들
  - 상수 개의 추가 공간만 사용

### 메모리 사용량 분석 🔍
```python
# Python
sys.getsizeof(int): 28bytes
sys.getsizeof(list): 기본 64bytes + 요소당 8bytes(참조)
```

```java
// Java
Integer: 16bytes
Stack<Integer>: 기본 40bytes + 요소당 16bytes
```

### 메모리 효율화 전략 💡
1. 불필요한 객체 생성 최소화
   - Python: 정수 캐싱 (-5 ~ 256)
   - Java: Integer 캐싱 (-128 ~ 127)\
2. 적절한 초기 용량 설정
   - ArrayList/Vector 사용 시 적절한 초기 용량 지정
3. 메모리 해제
   - Python: 명시적 del 사용
   - Java: 참조 해제 (null 할당)

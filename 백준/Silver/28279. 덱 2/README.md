# [Silver IV] 덱 2 - 28279 

[문제 링크](https://www.acmicpc.net/problem/28279) 

### 성능 요약

메모리: 72496 KB, 시간: 1060 ms

### 분류

자료 구조, 덱

### 제출 일자

2025년 1월 20일 01:32:10

### 문제 설명

<p>정수를 저장하는 덱을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.</p>

<p>명령은 총 여덟 가지이다.</p>

<ol>
	<li><span style="color:#e74c3c;"><code>1 X</code></span>: 정수 <var>X</var>를 덱의 앞에 넣는다. (1 ≤ <var>X</var> ≤ 100,000)</li>
	<li><span style="color:#e74c3c;"><code>2 X</code></span>: 정수 <var>X</var>를 덱의 뒤에 넣는다. (1 ≤ <var>X</var> ≤ 100,000)</li>
	<li><span style="color:#e74c3c;"><code>3</code></span>: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>4</code></span>: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>5</code></span>: 덱에 들어있는 정수의 개수를 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>6</code></span>: 덱이 비어있으면 <span style="color:#e74c3c;"><code>1</code></span>, 아니면 <span style="color:#e74c3c;"><code>0</code></span>을 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>7</code></span>: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>8</code></span>: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
</ol>

### 입력 

 <p>첫째 줄에 명령의 수 <var>N</var>이 주어진다. (1 ≤ <var>N</var> ≤ 1,000,000)</p>

<p>둘째 줄부터 <var>N</var>개 줄에 명령이 하나씩 주어진다.</p>

<p>출력을 요구하는 명령은 하나 이상 주어진다.</p>

### 출력 

 <p>출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.</p>

---
# Hyo's Memo 📚

## 📍 덱(Deque) 구현 방식 비교
> 양방향 큐를 구현하는 두 가지 방식: deque 모듈과 리스트 활용

### 1. 기본 구현 방식 🛠
#### Python 방식 1 (collections.deque)
```python
from collections import deque
deq = deque()  # 덱 생성
```

#### Python 방식 2 (list)
```python
numbers = []  # 리스트로 구현
```

#### Java 방식
```java
// 방식 1
Deque<Integer> deq = new ArrayDeque<>();

// 방식 2
ArrayList<Integer> numbers = new ArrayList<>();
```

### 2. 주요 연산 비교 ⚡
| 연산 | deque | list | 시간복잡도(deque) | 시간복잡도(list) |
|------|--------|------|------------------|-----------------|
| 앞에 추가 | `appendleft(x)` | `insert(0, x)` | O(1) | O(n) |
| 뒤에 추가 | `append(x)` | `append(x)` | O(1) | O(1) |
| 앞에서 제거 | `popleft()` | `pop(0)` | O(1) | O(n) |
| 뒤에서 제거 | `pop()` | `pop()` | O(1) | O(1) |
| 크기 확인 | `len(deq)` | `len(numbers)` | O(1) | O(1) |
| 비어있는지 확인 | `not deq` | `not numbers` | O(1) | O(1) |

### 3. 시간 복잡도 분석 ⏱️
#### deque 사용 시
- 모든 연산: O(1)
- 전체 프로그램: O(N)

#### list 사용 시
- 앞쪽 연산: O(N)
- 뒤쪽 연산: O(1)
- 전체 프로그램: O(N²)

### 4. 공간 복잡도 💾
- 두 방식 모두: O(N)
- deque가 약간 더 많은 메모리 사용
- N은 저장되는 요소의 수

### 5. 장단점 비교 📊
#### deque
- ✅ 모든 연산 O(1)
- ✅ 양방향 연산 최적화
- ⚠️ 추가 메모리 필요
- ⚠️ 모듈 import 필요

#### list
- ✅ 파이썬 기본 자료구조
- ✅ 직관적인 구현
- ⚠️ 앞쪽 연산 비효율
- ⚠️ 대용량 데이터에 취약

### 6. 사용 예시 💻
```python
# deque 방식
deq = deque()
deq.appendleft(1)  # 앞에 추가
deq.append(2)      # 뒤에 추가
deq.popleft()      # 앞에서 제거
deq.pop()          # 뒤에서 제거

# list 방식
numbers = []
numbers.insert(0, 1)  # 앞에 추가
numbers.append(2)      # 뒤에 추가
numbers.pop(0)         # 앞에서 제거
numbers.pop()          # 뒤에서 제거
```

### 7. 결론 💡
- 양방향 연산이 많은 경우: deque 사용 권장
- 간단한 구현/뒤쪽 연산 위주: list 사용 가능
- 성능 중요시: deque 필수
- 메모리 제한 엄격: list 고려

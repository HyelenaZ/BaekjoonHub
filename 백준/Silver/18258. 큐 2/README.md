# [Silver IV] 큐 2 - 18258 

[문제 링크](https://www.acmicpc.net/problem/18258) 

### 성능 요약

메모리: 112536 KB, 시간: 1392 ms

### 분류

자료 구조, 큐

### 제출 일자

2025년 1월 19일 01:38:14

### 문제 설명

<p>정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.</p>

<p>명령은 총 여섯 가지이다.</p>

<ul>
	<li>push X: 정수 X를 큐에 넣는 연산이다.</li>
	<li>pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>size: 큐에 들어있는 정수의 개수를 출력한다.</li>
	<li>empty: 큐가 비어있으면 1, 아니면 0을 출력한다.</li>
	<li>front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
</ul>

### 입력 

 <p>첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.</p>

### 출력 

 <p>출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.</p>

-------------------------------------------------------------------------------------------------------
# Hyo's Memo 📚

## 📍 Queue (큐) 연산 상세
> 기본적인 큐 연산의 구현 방법과 특징 정리

### 기본 구현 🛠
```python
# Python
from collections import deque
queue = deque()  # deque로 큐 구현
```

```java
// Java
Queue<Integer> queue = new LinkedList<>();
```

### 연산별 구현 방법 ⚡
#### Python 🐍
| 연산 | 구현 | 시간복잡도 |
|------|------|------------|
| push | `queue.append(x)` | O(1) |
| pop | `queue.popleft()` | O(1) |
| front | `queue[0]` | O(1) |
| back | `queue[-1]` | O(1) |
| empty | `len(queue) == 0` | O(1) |
| size | `len(queue)` | O(1) |

#### Java ☕
| 연산 | 구현 | 시간복잡도 |
|------|------|------------|
| push | `queue.offer(x)` | O(1) |
| pop | `queue.poll()` | O(1) |
| front | `queue.peek()` | O(1) |
| back | `((LinkedList)queue).getLast()` | O(1) |
| empty | `queue.isEmpty()` | O(1) |
| size | `queue.size()` | O(1) |

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
- ✅ deque 사용 필수 (일반 리스트의 pop(0)는 O(n))
- ⚠️ IndexError/NoSuchElementException 주의
- 💡 입력 최적화 고려

### 활용 팁 🎯
1. `startswith()` 사용으로 명령어 효율적 처리
2. 조건문 순서 최적화
3. 예외 처리는 필수

## 📍 복잡도 분석
### 시간 복잡도 ⏱️
- **큐 기본 연산**: 모두 O(1)
  - push/pop: O(1)
  - front/back: O(1)
  - empty/size: O(1)
- **전체 프로그램**: O(N)
  - N개의 명령을 각각 O(1)에 처리
  - N은 명령의 수 (1 ≤ N ≤ 10,000)

### 공간 복잡도 💾
- **큐 저장공간**: O(N)
  - 최악의 경우 N개의 push
  - 각 원소는 정수 (1 ≤ X ≤ 100,000)
- **추가 변수**: O(1)
  - 명령어 처리용 임시 변수들

### 메모리 사용량 분석 🔍
```python
# Python
sys.getsizeof(int): 28bytes
sys.getsizeof(deque): 기본 648bytes + 요소당 8bytes
```
```java
// Java
Integer: 16bytes
LinkedList: 기본 24bytes + 요소당(Node) 24bytes
```

### 메모리 효율화 전략 💡
1. **deque 사용**
   - 양방향 접근 O(1)
   - 내부 최적화
2. **입력 버퍼 활용**
   - sys.stdin.readline
   - 문자열 처리 최소화
3. **불필요한 변수 제거**
   - 임시 변수 재사용
   - 즉시 처리 활용

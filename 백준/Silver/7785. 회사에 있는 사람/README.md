# [Silver V] 회사에 있는 사람 - 7785 

[문제 링크](https://www.acmicpc.net/problem/7785) 

### 성능 요약

메모리: 42656 KB, 시간: 200 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵

### 제출 일자

2025년 1월 21일 12:45:13

### 문제 설명

<p>상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.</p>

<p>각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.</p>

<p>상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 10<sup>6</sup>) 다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.</p>

<p>회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.</p>

### 출력 

 <p>현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.</p>

---
# Hyo's Memo 📚

## 📍 문제 유형: 자료구조 (Set/HashSet)
> 회사 출입 기록을 효율적으로 관리하는 문제

### 1. 핵심 요구사항 분석 🎯
- 실시간 출입 상태 관리 (enter/leave)
- 중복 없는 이름 관리
- 최종 결과 역순 정렬 출력

### 2. 최적 자료구조 선택 ⚡
#### Set 선택 이유
- 중복 제거 자동 처리
- O(1) 시간 복잡도의 추가/제거
- 메모리 효율성

### 3. 언어별 구현 방법 🛠

#### Python 구현 🐍
```python
# 1. 기본 구현
office = set()  # 생성
office.add(name)  # 추가
office.remove(name)  # 제거
sorted(office, reverse=True)  # 정렬

# 2. 최적화 구현
from sortedcontainers import SortedSet
office = SortedSet(reverse=True)  # 자동 정렬 관리
```

#### Java 구현 ☕
```java
// 1. HashSet 구현
HashSet<String> office = new HashSet<>();
office.add(name);
office.remove(name);
TreeSet<String> sorted = new TreeSet<>(Comparator.reverseOrder());
sorted.addAll(office);

// 2. TreeSet 구현 (자동 정렬)
TreeSet<String> office = new TreeSet<>(Collections.reverseOrder());
```

### 4. 핵심 메서드 비교 📊

#### Python 메서드
| 메서드 | 시간복잡도 | 설명 |
|--------|------------|------|
| `add()` | O(1) | 요소 추가 |
| `remove()` | O(1) | 요소 제거 (없으면 KeyError) |
| `discard()` | O(1) | 요소 제거 (없어도 에러 없음) |
| `sorted()` | O(n log n) | 정렬된 리스트 반환 |

#### Java 메서드
| 메서드 | HashSet | TreeSet | 설명 |
|--------|----------|----------|------|
| `add()` | O(1) | O(log n) | 요소 추가 |
| `remove()` | O(1) | O(log n) | 요소 제거 |
| `contains()` | O(1) | O(log n) | 요소 검색 |

### 5. 성능 분석 📈

#### 시간 복잡도
```python
# 전체 시간 복잡도: O(n log n)
1. 입력 처리: O(n)
2. Set 연산: O(1) * n = O(n)
3. 정렬: O(n log n)
```

#### 공간 복잡도
```python
# 전체 공간 복잡도: O(n)
1. Set 저장: O(n)
2. 정렬 임시 공간: O(n)
```

### 6. 최적화 전략 💡

#### 입력 최적화
```python
# Python
import sys
input = sys.stdin.readline

# Java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```

#### 자료구조 최적화
```python
# Python: SortedSet 사용
from sortedcontainers import SortedSet
office = SortedSet()  # 삽입 시 자동 정렬

# Java: TreeSet 사용
TreeSet<String> office = new TreeSet<>(Collections.reverseOrder());
```

### 7. 주의사항 ⚠️

#### Python
- ✅ `set`은 해시 테이블 기반으로 빠른 연산
- ⚠️ `remove()`는 키 없으면 KeyError 발생
- 💡 `discard()`로 안전한 제거 가능
- 🔍 정렬은 별도 처리 필요

#### Java
- ✅ `HashSet`은 순서 보장 없음
- ⚠️ `TreeSet`은 정렬 자동화로 삽입/삭제 시 약간의 오버헤드
- 💡 정렬이 필요한 경우 `TreeSet` 권장
- 🔍 Multi-thread 환경에서는 `ConcurrentHashMap` 고려

### 8. 최종 최적화 코드 💻

## 📍 Set의 remove()와 discard() 메서드 비교

### 기본 동작 차이 🔍

```python
# remove() 예시
s = {1, 2, 3}
s.remove(2)      # {1, 3}
s.remove(2)      # KeyError: 2  <- 에러 발생!

# discard() 예시
s = {1, 2, 3}
s.discard(2)     # {1, 3}
s.discard(2)     # {1, 3}  <- 에러 없음!
```

### 주요 특징 비교 ⚡
| 특징 | remove() | discard() |
|------|----------|-----------|
| 존재하는 요소 제거 | O(1) | O(1) |
| 없는 요소 제거 시도 | KeyError 발생 | 아무 일도 일어나지 않음 |
| 예외 처리 필요성 | 필요 | 불필요 |

### remove() 사용이 적절한 경우 ✅
```python
try:
    in_office.remove(name)
except KeyError:
    print(f"Error: {name} is not in office")
```
- 요소가 반드시 있어야 하는 경우
- 없는 요소 제거 시도를 오류로 처리해야 하는 경우
- 디버깅이 필요한 경우

### discard() 사용이 적절한 경우 ✅
```python
in_office.discard(name)  # 간단하고 안전
```
- 요소의 존재 여부가 확실하지 않은 경우
- 에러 처리가 불필요한 경우
- 코드를 더 간결하게 작성하고 싶은 경우
#### Python 최종 버전
```python
import sys
input = sys.stdin.readline

def process_logs():
    n = int(input())
    office = set()
    
    for _ in range(n):
        name, status = input().split()
        if status == "enter":
            office.add(name)
        else:
            office.discard(name)
            
    return sorted(office, reverse=True)

# 실행 및 출력
for name in process_logs():
    print(name)
```

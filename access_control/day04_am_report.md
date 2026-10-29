# 3과목 Day 4 접근 점검 · 필요 없어진 권한 찾기 · 오전 (이름 · 2026-10-29(목))

> **쓰는 법**
> - 문제를 풀 때마다 그 문제 제목 아래 질문에 답합니다.
> - 질문마다 `쓸 내용:` 에 무엇을 쓰면 되는지 적혀 있습니다. 그대로 `답:` 뒤에 씁니다.
> - 출력이나 코드를 붙여 넣는 질문은 `답:` 아래 빈 코드 상자에 붙여 넣고, 설명은 `답:` 뒤에 씁니다.
> - 「왜」를 묻는 질문은 한 단어로 끝내지 말고, 내 화면에서 본 값이나 배운 내용을 근거로 이유까지 씁니다.
> - 🔍 는 이 교시에서 꼭 알아야 할 핵심 질문입니다. 답을 못 찾았으면 「모름 — 막힌 곳: …」 이라고 씁니다. 🔍 가 없는 질문도 못 적으면 같은 말을 씁니다.

---

## 2교시 · 지금 부여돼 있는 권한 현황 만들기

### 문제 2-1 · 역할과 예외를 합쳐 지금 부여돼 있는 권한 현황 만들기

- (가) 실행한 출력 전체를 붙여 넣고, 부여돼 있는 권한이 모두 몇 건인지, 그중 예외로 받은 권한이 몇 건인지, 현황에 권한이 하나도 없는 사용자가 있다면 누구이고 그 이유는 무엇인지 적어 주세요.
  - 쓸 내용: ① 출력 전체(코드 상자에 붙여 넣기) ② 전체 건수 ③ 예외로 받은 건수 ④ 권한이 하나도 없는 사용자와 그 이유
  - 답:

```
--- 단계 1: 현황 - 부여돼 있는 권한 14 건
seoyeon SALES:QUERY <- 역할 sales | 재직 True
seoyeon SALES:CHANGE <- 역할 sales | 재직 True
junho SALES:QUERY <- 역할 finance | 재직 True
junho SETTLE:QUERY <- 역할 finance | 재직 True
gaeun ACCOUNT:QUERY <- 역할 account_admin | 재직 True
gaeun ACCOUNT:CHANGE <- 역할 account_admin | 재직 True
dami SALES:QUERY <- 역할 sales | 재직 False
dami SALES:CHANGE <- 역할 sales | 재직 False
batch-night SETTLE:QUERY <- 역할 batch | 재직 True
seoyeon SETTLE:QUERY <- 예외 1번 | 재직 True
junho SALES:CHANGE <- 예외 2번 | 재직 True
dami SALES:QUERY <- 예외 3번 | 재직 False
batch-night SALES:QUERY <- 예외 4번 | 재직 True
gaeun SETTLE:QUERY <- 예외 5번 | 재직 True
--- 단계 2: 점검 - 사용자별 권한 개수
{'seoyeon': 3, 'junho': 3, 'gaeun': 3, 'dami': 3, 'batch-night': 2}
```

- (나) 🔍 현황 목록에는 판정 함수(`check_permission` · `evaluate_access`)가 이미 거부하는 권한도 들어 있습니다. 어떤 권한이 그런지 예를 하나 들고, 거부되는 권한을 목록에서 빼지 않고 남겨 두는 것이 점검에 왜 필요한지 적어 주세요.
  - 쓸 내용: ① 이미 거부되는 권한의 예 ② 남겨 두는 이유
  - 답:

## 3교시 · 규칙으로 필요 없어진 권한 찾기

### 문제 3-1 · 현황에서 퇴사한 계정과 만료된 예외 찾기

- (가) 실행한 출력 전체를 붙여 넣고, 규칙에 걸린 권한이 이유별로 몇 건인지 적어 주세요.
  - 쓸 내용: ① 출력 전체(코드 상자에 붙여 넣기) ② 이유별 건수
  - 답:

```
--- 단계 1: 판정 - 규칙에 걸린 권한 7 건 (전체 14 건 중)
dami SALES:QUERY <- 역할 sales | 퇴사한 계정
dami SALES:CHANGE <- 역할 sales | 퇴사한 계정
seoyeon SETTLE:QUERY <- 예외 1번 | 만료된 예외
junho SALES:CHANGE <- 예외 2번 | 만료된 예외
dami SALES:QUERY <- 예외 3번 | 퇴사한 계정
batch-night SALES:QUERY <- 예외 4번 | 만료된 예외
gaeun SETTLE:QUERY <- 예외 5번 | 만료된 예외
--- 단계 2: 점검 - 이유별 건수
{'퇴사한 계정': 3, '만료된 예외': 4}
```

- (나) 🔍 퇴사한 계정과 만료된 예외는 파일에 적힌 사실로 걸러 냈습니다. 이 규칙으로는 걸러 낼 수 없지만 필요 없을 수 있는 권한의 예를 하나 들고, 그것을 찾으려면 어떤 정보가 더 필요한지 적어 주세요.
  - 쓸 내용: ① 규칙으로 못 거르는 권한의 예 ② 찾는 데 필요한 정보
  - 답:

- (다) 🔍 규칙에 걸린 7건을 내일 회수한다면 어떤 것부터 회수할까요? 출력의 이유(퇴사한 계정 · 만료된 예외)를 보고 기준을 하나 정해, 그 기준으로 이유를 적어 주세요.
  - 쓸 내용: ① 먼저 회수할 것 ② 그 기준과 이유
  - 답:

## 4교시 · 사용 이력으로 90일 넘게 안 쓴 권한 찾기

### 문제 4-1 · 사용 이력으로 90일 넘게 안 쓴 권한 후보 찾기

- (가) 실행한 출력 전체를 붙여 넣고, 90일 넘게 안 쓴 후보가 몇 건인지와 후보마다 며칠째 안 쓰였는지 적어 주세요.
  - 쓸 내용: ① 출력 전체(코드 상자에 붙여 넣기) ② 후보 건수 ③ 후보별 안 쓴 일 수(이력이 없으면 「이력 없음」)
  - 답:

```
--- 단계 1: 현황 - 규칙에 안 걸린 권한 7 건의 안 쓴 일 수
seoyeon SALES:QUERY -> 2 일째 안 씀
seoyeon SALES:CHANGE -> 120 일째 안 씀
junho SALES:QUERY -> 91 일째 안 씀
junho SETTLE:QUERY -> 90 일째 안 씀
gaeun ACCOUNT:QUERY -> 9 일째 안 씀
gaeun ACCOUNT:CHANGE -> 사용 이력 없음
batch-night SETTLE:QUERY -> 0 일째 안 씀
--- 단계 2: 판정 - 90일 넘게 안 쓴 후보 3 건
seoyeon SALES:CHANGE <- 역할 sales
junho SALES:QUERY <- 역할 finance
gaeun ACCOUNT:CHANGE <- 역할 account_admin
```

- (나) 🔍 junho 의 `SETTLE:QUERY` 는 마지막 사용이 90일 전이라 후보에서 빠졌고, 같은 junho 의 `SALES:QUERY` 는 91일 전이라 후보에 들어갔습니다. 하루 차이로 나누는 기준은 합리적일까요? 경계 부근에서 담당자가 추가로 확인할 것도 적어 주세요.
  - 쓸 내용: ① 합리적인지와 이유 ② 추가로 확인할 것
  - 답: 경계값을 90일로 설정. 경계값 안에 포함되면 넣고, 아니면 제외

- (다) 🔍 사용 이력이 없는 권한을 바로 지우면 위험한 경우가 있습니다. 어떤 경우인지 예를 들고, 지우기 전에 무엇을 확인해야 하는지 적어 주세요.
  - 쓸 내용: ① 위험한 경우의 예 ② 지우기 전에 확인할 것
  - 답: 


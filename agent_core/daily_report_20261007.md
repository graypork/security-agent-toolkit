# 야간 보안 관제 보고 (2026-10-07)

## 한눈에 보기
- 처리한 경보: 18건 (high 6건)
- **주의: high 경보 6건 — 건별 내역을 먼저 확인할 것**

## 총평
밤사이 최고 수준의 심각한 보안 경보가 다수 발생하여 각별한 주의가 필요합니다. 특히 관리자 계정의 무단 생성과 로그인 탈취 의심 정황이 포착되었으므로, 즉각적인 계정 보안 점검과 대응 조치를 시행하겠습니다.

## 건별 내역 (위험한 것부터)
- [HIGH] E01 admin 계정에 로그인 실패 4회
- [HIGH] E02 실패 직후 admin 로그인 성공 — 탈취 의심
- [HIGH] E03 한 IP 의 비밀번호 스프레잉
- [HIGH] E04 root 계정에 로그인 실패 6회
- [HIGH] E12 guest01 의 shadow 접근 거부
- [HIGH] E16 관리자 권한 계정 무단 생성 의심
- [MEDIUM] E05 svc_backup 의 sudoers 접근 거부
- [MEDIUM] E08 deploy 토큰 만료
- [MEDIUM] E09 guest 계정에 로그인 실패 5회
- [MEDIUM] E10 lee.yh 새 IP 로그인
- [MEDIUM] E13 외부 IP 의 포트 스캔
- [MEDIUM] E15 svc_batch 새벽 로그인 실패
- [LOW] E06 kim01 로그인 실패 1회
- [LOW] E07 park.js 실패 뒤 정상 로그인
- [LOW] E11 choi.mk 로그인 실패 2회
- [LOW] E14 jung.hw 로그인 실패 1회
- [LOW] E17 kim.cs 로그인 실패 1회
- [LOW] E18 점검 중 방화벽 규칙 수정

# [Captured] Project Glasswing: An Initial Update

> ⚠️ 이 파일은 verbatim 원문이 아닌 **구조화된 추출** 입니다. WebFetch가 저작권 사유로 전문 복제를 거부하여, factual content를 정리한 형태로 보존합니다. 원문은 항상 아래 URL을 참조.

- **원문 URL**: https://www.anthropic.com/research/glasswing-initial-update
- **발행일**: 2026-05-22
- **작성**: Anthropic research team (개별 저자 미명시)
- **캡처일**: 2026-05-25
- **타입**: research blog post

---

## 메인 thesis

Anthropic의 Project Glasswing — ~50개 파트너와의 협업 사이버보안 이니셔티브 — 가 Claude Mythos Preview를 활용해 critical 소프트웨어에서 high/critical-severity 취약점 10,000개 이상을 발견. 사이버보안의 근본적 전환을 시사: **취약점 발견은 빨라졌지만, 검증·공개·패치는 인간의 capacity가 병목**.

## 핵심 통계

### 취약점 발견
- 10,000+ high/critical-severity 취약점 (전체 파트너 합산)
- Cloudflare: 2,000 버그 (400개가 high/critical)
- Mozilla: Firefox 150에서 271개 (Opus 4.6의 Firefox 148 대비 10배)
- 오픈소스 1,000+ 프로젝트에서 6,202 high/critical (전체 23,019)
- 현재 검증율로 추정 시 오픈소스에서 ~3,900개 high/critical 예상

### 검증
- 외부 firm이 1,752개 평가
- 90.6% (1,587) true positive
- 62.4% (1,094) high/critical로 재확인

### 패치
- 530개 high/critical을 maintainer에 보고
- 75개 패치 배포, 65개 공개 advisory
- 평균 패치 개발 기간 2주
- Claude Opus 4.7이 엔터프라이즈 취약점 2,100+개를 3주 만에 패치

### 파트너 성과
- Cloudflare: 버그 발견율 10배 증가
- Palo Alto Networks: 평소 대비 5배 패치
- Oracle: 발견 속도 수 배 증가

### 금융 영향
- Glasswing 파트너 은행에서 $1.5M 사기 송금 사전 차단

## 등장 조직

**Glasswing 파트너**: Anthropic, Cloudflare, Mozilla, Oracle, Microsoft, Palo Alto Networks, Cisco, 적격 엔터프라이즈·은행

**외부 평가**: UK AI Security Institute (AISI), XBOW, Open Source Security Foundation (Alpha-Omega), Linux Foundation, NIST, UK NCSC

**기타 언급**: ExploitBench, ExploitGym, wolfSSL (CVE-2026-5194 예시)

## 등장 모델

- **Claude Mythos Preview**: 주역. AISI 사이버 레인지 양쪽을 end-to-end로 해결한 첫 모델. XBOW 평가에서 "기존 모든 모델 대비 significant step up". 일반 공개 안 됨 (안전 안전장치 미흡).
- **Claude Opus 4.6**: 비교 baseline (이전 세대)
- **Claude Opus 4.7**: 현재 공개 플래그십. 엔터프라이즈 취약점 패치에 활용.
- Claude Haiku, Claude Sonnet (지나가는 언급)

## 섹션 구조

1. Announcements
2. Our Early Results
   - Mythos Preview 발견에 대한 논의 접근법
   - 파트너 및 외부 테스터 증거
3. Open-source Software
4. Adapting to a New Phase of Cybersecurity
   - 공개 모델로 cyberdefense 도구 만들기
5. Supporting the Ecosystem
6. What's Next for Project Glasswing

## 방법론

- Mythos Preview가 코드베이스 스캔으로 취약점 식별
- 모델이 functional exploit을 구성하여 발견을 검증
- 예: wolfSSL — 인증서 위조로 사기 사이트 호스팅 가능한 exploit 생성
- 보안 firm 또는 Anthropic이 재현·심각도 재평가·기존 fix 확인 후 maintainer에 상세 리포트
- Cloudflare 보고: false positive 비율이 인간 테스터보다 낮음

### 제공 도구
- Claude Security (엔터프라이즈 public beta)
- 반복적 취약점 스캐닝용 custom skills
- 코드베이스 매핑·서브에이전트 스캐닝 harness
- 위협 모델 빌더 (공격 대상 식별)
- Foundry Security Spec (Cisco가 오픈소스화)

### 공개 절차
- 90일 coordinated disclosure window (패치 조기 작성 시 45일)
- 취약점이 triage/patching 단계를 통과하는 추적 대시보드

## 도전과 한계

### 주요 변화
> "Now it's limited by how quickly we can verify, disclose, and patch the large numbers of vulnerabilities found by AI."

### 생태계 병목
- Maintainer capacity 제약, 일부는 disclosure 속도 감속 요청
- 오픈소스 maintainer가 저품질 AI-generated 버그 리포트에 압도되는 문제
- 발견·패치·배포 간 lag → exploit window
- 검증에 집약적 인적 노력 필요

### 안전장치 격차
> "No company has developed safeguards strong enough to prevent such models from being misused."

- Mythos-class 모델은 안전장치 미흡으로 공개 안 함
- 경쟁사가 안전장치 없이 유사 모델을 공개할 위험

### 패치 배포 지연
- 발견부터 광범위 배포까지의 window
- 최종 사용자의 SW 업데이트 설치가 여전히 난제

## 향후 계획

### 단기
- 미국·동맹국 정부와 협력하여 Glasswing 파트너 확대
- 오픈소스 코드 스캐닝 지속
- CVE 공개 기간 후 패치 완료된 취약점의 상세 기술 분석 공개
- 적격 고객 보안 팀에 도구·리소스 제공
- ExploitBench, ExploitGym 등 고품질 정량 벤치마크 개발 지원

### 중기
- CVE-2026-5194 (wolfSSL) 전체 기술 분석 수 주 내 공개
- 파트너십 성과 패치 확대 배포

### 장기 비전
- Mythos-class 모델용 안전장치 강화 후 일반 공개
- 개발자가 배포 전 버그를 잡을 수 있게 함
- 임시적 고위험 패치 시기 → 강화된 SW와 해킹 감소 시대로 전환

### 지속 약속
- Claude for Open Source: maintainer 지원
- Anthropic이 채택한 오픈소스 패키지 스캔 commit
- OSSF Alpha-Omega 협력
- External Researcher Access Program

## 핵심 인용

> "Now it's limited by how quickly we can verify, disclose, and patch the large numbers of vulnerabilities found by AI."

> "Several have told us that their rate of bug-finding has increased by more than a factor of ten."

> "No company has developed safeguards strong enough to prevent such models from being misused."

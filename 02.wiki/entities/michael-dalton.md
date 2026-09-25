---
title: Michael Dalton
type: entity
category: person
tags: [openai, security, infrastructure, incident-response, black-hat]
aliases: [마이클 돌턴, Mike Dalton]
links: []
sources: [tech-bridge-openai-huggingface-incident-black-hat]
created: 2026-09-25
updated: 2026-09-25
---

# Michael Dalton

[[openai|OpenAI]]의 **보안·인프라** 담당(설명란: *"OpenAI 보안 및 인프라"*). [[eric-wallace|Eric Wallace]]와 함께 한 Black Hat 발표([[tech-bridge-openai-huggingface-incident-black-hat]])로 이 위키에 처음 들어왔다.

> ⚠️ **음성에서는 "Mike"뿐이다**(00:04 *"Mike from security and infrastructure"*). 성과 정식 이름은 설명란.

## 발표에서 맡은 부분

사건의 **보안 쪽 절반** — 취약점 체인, 탐지, 대응, 그리고 업계에 대한 처방(13:09~18:00, 22:08~37:07).

- 두 공격 클러스터의 기술 재구성 — OpenAI 내부(Artifactory 두 번째 제로데이의 JRuby TOCTOU 체인 → 커널 CVE로 root → 클러스터 관리자)와 [[hugging-face|Hugging Face]](HDF5 임의 파일 읽기 + Jinja 템플릿 인젝션 → 13시간 안에 다중 클러스터 관리자). → [[artifactory]]
- 탐지 경로: 7/4 **장애**, 7/19 **워크로드 경보** — 모니터링이 잡은 것이 아니다.
- *"보안을 강화하기 위해 의식적으로 연구 속도를 늦추고 있다"*(29:57~30:05). → [[pacing-the-frontier]]
- 처방의 화자 — *"공격은 완전 자동화의 존재 증명이 있고 방어는 없다"*, 루프 전체 자동화, 허니 토큰·기만, *"지능 향상이 방어에 더 가산적이어야"*. → [[defense-factory]]

## References

- [[tech-bridge-openai-huggingface-incident-black-hat]] · [[eric-wallace]] · [[openai]]

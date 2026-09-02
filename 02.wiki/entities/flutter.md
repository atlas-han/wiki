---
title: Flutter
type: entity
category: tool
tags: [flutter, dart, cross-platform, mobile, ui-framework, google]
aliases: [플러터]
links:
  - https://flutter.dev
  - https://goo.gle/4yfeaRB
sources: [tech-bridge-flutter-ai-workflow]
created: 2026-09-02
updated: 2026-09-02
---

# Flutter

Google의 크로스플랫폼 UI 프레임워크. Dart 언어로 **하나의 코드베이스**에서 Android·iOS·Windows·macOS·웹 등을 빌드한다. 본 위키 첫 등장은 [[ivanna-kacevica|Ivanna Kaceviča]]의 인터뷰 [[tech-bridge-flutter-ai-workflow]] (2026-09-02) — 위키 첫 **모바일/크로스플랫폼 프레임워크** 축.

## 위키에서 알려진 사실 (AI 코딩 관점)

- **학습 데이터 격차**: *"학습 데이터 확보 측면에서 Flutter는 Python이나 JavaScript에 비해 한참 뒤떨어지기 때문에"* Row·Column 같은 기본 레이아웃 지식을 에이전트에 반복해서 줘야 한다. 강한 모델도 컨테이너+패딩 조합이나 하드코딩된 Positioned를 선호하는 경향이 관찰됐다. → 발표자는 Row·Column·Wrap·Stack의 **사용 시점**을 작은 [[agent-skills|스킬]]로 둔다. [[sutton-bitter-lesson]]의 학습 데이터 축 반례.
- **공식 스킬**: Google 저장소에 Flutter 스킬·Dart 공식 스킬이 있고, 진행자(Flutter 팀)에 따르면 팀원 한 명이 작성했으며 유지보수가 *"새 저장소 하나만큼"* 든다. 발표자는 프롬프트 인젝션 위험이 낮은 **공식 출처**로 이를 권한다 ([[prompt-injection]]).
- **Flutter AI rules**: 채널 설명란이 <https://goo.gle/4yfeaRB>를 링크한다. 내용은 이 위키가 ingest하지 않았다.
- **골든 테스트 vs 실제 스크린샷**: 골든 테스트는 폰트·이미지 로딩 손질이 필요해 **회귀** 잡기에 쓰고, QA는 웹에서 띄운 앱의 실제 스크린샷(애니메이션 webp 포함)을 **다른 에이전트가 시각 검사**한다 ([[generator-evaluator-pattern]]).
- **레버리지 논증**: *"하나 값에 둘"* — 에이전트가 코드를 싸게 쓰는 세계에서 한 코드베이스가 닿는 플랫폼 수(최소 4)가 곱해지는 계수가 된다.
- Fluttercon(설명란: Fluttercon USA '26)이 인터뷰 장소로 추정된다.

> 프레임워크 자체의 아키텍처·위젯 모델은 이 위키에 ingest된 바 없다. 위 내용은 AI 워크플로 인터뷰 한 편에 근거한다.

## References

- [[tech-bridge-flutter-ai-workflow]] — [[ivanna-kacevica]], 2026-09-02
- 외부: <https://flutter.dev> · Flutter AI rules <https://goo.gle/4yfeaRB> · Flutter 공식 채널 <http://goo.gle/FlutterYT>

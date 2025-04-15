# 🛠 FastAPI 기반 REST API 프로젝트

## 📌 프로젝트 개요
이 프로젝트는 FastAPI를 활용하여 REST API 개발을 연습하기 위한 프로젝트입니다.  
사용자는 JWT 인증을 통해 로그인하고 CRUD 기능을 수행할 수 있습니다.  

## 🚀 주요 기능
- JWT 기반 인증 (OAuth2)
- CRUD API (유저 관리, 게시글 관리)
- Docker 컨테이너 환경 구성
- PostgreSQL 연동 및 ORM(SQLAlchemy) 활용

## ⚙️ 기술 스택
- FastAPI, Python
- PostgreSQL, SQLAlchemy
- Docker, CI/CD
- OAuth2, JWT


## 🔧 실행 방법
```bash
# 가상환경 생성 & 패키지 설치
python -m venv .venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt

# 환경 변수 설정 (.env 파일 필요)
cp .env.example .env

# 서버 실행
uvicorn main:app --reload
```

```
fast-rest-test/
├── backend/                    # FastAPI 백엔드
│   ├── .venv/
│   ├── app/
│   │   ├── api/               # 라우터 모음
│   │   ├── core/              # 설정, 보안, 의존성 등
│   │   ├── models/            # SQLAlchemy 모델
│   │   ├── schemas/           # Pydantic 스키마
│   │   ├── services/          # 비즈니스 로직
│   │   ├── push/              # FCM 푸시 관련
│   │   ├── main.py            # FastAPI 앱 실행
│   │   └── config.py          # 환경변수 설정
│   ├── alembic/               # 마이그레이션 도구
│   ├── tests/                 # 유닛/통합 테스트
│   ├── requirements.txt
│   └── Dockerfile
│
├── mobile-app/                # React Native 앱
│   ├── src/
│   │   ├── screens/
│   │   ├── components/
│   │   ├── navigation/
│   │   ├── api/               # Axios 등 API 클라이언트
│   │   ├── hooks/
│   │   └── utils/
│   ├── assets/
│   ├── App.tsx
│   ├── app.json
│   ├── .env
│   └── package.json
│
│
├── docs/                      # 명세 및 문서
│   ├── API_SPEC.md            # 전체 API 명세
│   ├── DB_SCHEMA.md           # DB 설계 (ERD 포함)
│   ├── IA_STRUCTURE.md        # 서비스 IA 문서
│   ├── FEATURE_LIST.md        # 기능 정의서
│   └── ISSUE_LIST.md          # 작업 분해표
│
├── .env
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Issue List

	FastAPI (BE) + React Native (FE) + MySQL + JWT 인증 기반 플랫폼
	전체 개발 작업 분해표 (Issue List) 

0. 프로젝트 환경 세팅
- [ ] FastAPI 프로젝트 구조 생성
- [ ] MySQL 연결 (SQLAlchemy + Alembic)
- [ ] JWT 인증 시스템 구축
- [ ] Docker + docker-compose 세팅
- [ ] Swagger 자동 문서화 설정

1. 유저 (소비자) 기능
- [ ] 회원가입 (이메일 / 소셜 로그인 - 카카오)
- [ ] 로그인 + JWT 토큰 발급
- [ ] 마이페이지 (내 예약 목록, 프로필 편집)
- [ ] 푸시 알림 토큰 등록 API
- [ ] 회원탈퇴 / 비활성화

2. 서비스 공급자 (청소 기사) 기능
- [ ] 기사 회원가입 (정보 입력 + 인증 문서 업로드)
- [ ] 기사 로그인
- [ ] 본인 서비스 지역 설정
- [ ] 예약 수락 / 거절 기능
- [ ] 내 스케줄 조회
- [ ] 후기 열람

3. 예약 시스템
- [ ] 서비스 카테고리 (에어컨 종류 등)
- [ ] 예약 요청 생성
- [ ] 예약 가능한 기사 리스트 매칭
- [ ] 기사 선택 → 예약 확정
- [ ] 예약 상태 관리 (요청 → 수락 → 완료)
- [ ] 캘린더 뷰 API

4. 관리자/운영 기능 (추후 확장용)
- [ ] 서비스 통계 API
- [ ] 유저/기사 블라인드 처리
- [ ] 리뷰 모니터링

5. 공통 / 인프라
- [ ] 예외처리 통일 (FastAPI exception handler)
- [ ] 로깅 시스템 (Loguru or Sentry)
- [ ] 환경변수 관리 (.env)
- [ ] API 테스트용 Postman Collection export
- [ ] CI/CD 파이프라인 (GitHub Actions)

6. 프론트엔드 작업 (React Native)
- [ ] 기본 폴더 구조 세팅
- [ ] 로그인/회원가입 화면
- [ ] 기사 리스트 / 상세 / 예약 흐름 UI
- [ ] 예약 캘린더 뷰
- [ ] 결제 화면 연동
- [ ] 후기 작성 UI
- [ ] 알림 처리 (Firebase FCM)
- [ ] 앱 아이콘 / 스플래시 / 설정 등

7. QA 및 테스트
- [ ] API 통합 테스트 (pytest)
- [ ] FE 통신 테스트 (Postman 기반)
- [ ] 유저 플로우 전체 E2E 검증
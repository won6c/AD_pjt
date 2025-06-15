# 📚 AI 추천 기반 도서관 시스템 + 🎮 맵 & 게임 연동 웹서비스

이 프로젝트는 Django 기반 웹 애플리케이션으로, **도서 검색·추천**, **캐릭터 맵 이동**, **게임 플레이**, **도서 대출 및 평점 기록**, **다중 로그인 감지**, **마이페이지 요약** 기능까지 통합된 **종합적인 도서관 경험**을 제공합니다.

<br/>

## 🚀 주요 기능 (Features)

### 📖 도서 서비스
- 키워드 기반 도서 검색 (제목, 작가, 장르)
- 콘텐츠 기반 도서 추천 (TF-IDF 유사도 분석)
- 도서 대출 / 반납 기록 관리
- 도서 평점 등록 및 평균 평점 계산

### 🎮 게임 시스템
- js-DOS 기반 고전 게임 **DOOM** 연동
- 플레이 시간 자동 기록 (2분 단위)
- 게임 결과를 DB에 저장하여 추적

### 🧍 캐릭터 & 맵
- 회원가입 시 캐릭터 선택 (3종 스프라이트 제공)
- Phaser 기반 2D 도서관 맵 구현
- 캐릭터가 직접 이동하여 도서 검색/로비로 진입 가능
- 캐릭터 변경은 마이페이지에서 가능

### 🧑‍💻 마이페이지
- 내 대출 기록 확인
- 내가 작성한 Q&A 게시글 목록 확인
- 캐릭터 변경 가능

### 🔒 보안 기능
- Django 세션 기반 로그인 시스템
- 동일 계정 다중 로그인 탐지 (`user_logged_in` 시그널 감지)

---

## 🧱 기술 스택 (Tech Stack)

| 구성 요소 | 사용 기술 |
|----------|-----------|
| Backend | Django 4.x, Django REST Framework |
| Frontend | HTML5, Bootstrap5, JavaScript, jQuery |
| Game Engine | Phaser 3, js-DOS |
| AI 추천 | Scikit-learn TF-IDF |
| Database | PostgreSQL |
| 인증/보안 | Django Auth, Session, CSRF 보호 |
| 기타 | Pillow, static/media 관리 |

---

## 📂 프로젝트 구조

```
djangobook/
├── api/               # 도서 평점 및 게임 기록 API
├── common/            # 회원가입, 로그인, 마이페이지
├── config/            # Django 설정
├── game/              # DOOM 게임 실행 및 기록 저장
├── library/           # 도서 검색/추천/대출/평점 기능
├── pybo/              # 질문/답변 게시판 기능
├── static/            # 캐릭터 스프라이트, 배경 맵, Doom 파일
├── logs/            # activity log
└── templates/         # HTML 템플릿 파일
```

---

## ⚙️ 설치 및 실행 방법

```bash
# 1. 프로젝트 클론
git clone https://github.com/your-id/your-project-name.git
cd your-project-name

# 2. 가상환경 설정 및 의존성 설치
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. 마이그레이션 및 서버 실행 ( cert.pem & key.pem은 생성해야 함 )
python manage.py migrate
python manage.py runsslserver --certificate cert.pem --key key.pem 

```

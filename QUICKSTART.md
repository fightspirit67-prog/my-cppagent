# 🚀 빠른 시작 가이드

## 1️⃣ API 키 받기

1. [Anthropic Console](https://console.anthropic.com/) 접속
2. 로그인 후 API Keys 메뉴로 이동
3. "Create Key" 버튼 클릭
4. 생성된 API 키 복사 (sk-ant-api03-로 시작)

## 2️⃣ API 키 설정

### Windows 사용자
```cmd
# 1. config.ini.example을 config.ini로 복사
copy config.ini.example config.ini

# 2. 메모장으로 config.ini 열기
notepad config.ini

# 3. 아래처럼 API 키 입력 후 저장
CLAUDE_API_KEY=sk-ant-api03-여기에붙여넣기

# 4. 프로그램 실행
run.bat
```

### Mac/Linux 사용자
```bash
# 1. config.ini 파일 생성
cp config.ini.example config.ini

# 2. 편집기로 열기
nano config.ini
# 또는
vim config.ini

# 3. API 키 입력 후 저장
CLAUDE_API_KEY=sk-ant-api03-여기에붙여넣기

# 4. 프로그램 실행
./run.sh
```

## 3️⃣ 프로그램 사용법

### 연습 문제 풀기
1. 왼쪽 사이드바에서 난이도 선택 (초급부터 시작 추천)
2. 문제 제목 클릭
3. Claude가 자동으로 문제 설명과 힌트 제공
4. 하단 입력창에 질문이나 코드 작성
5. "전송" 버튼 클릭 또는 Enter 키

### 자유 질문하기
- 하단 입력창에 C++ 관련 질문 입력
- 예: "class와 struct는 언제 써야 해?"
- 예: "이 코드를 리뷰해줘: [코드 붙여넣기]"

### 대화 초기화
- 새로운 주제로 시작하고 싶을 때
- 왼쪽 하단 "🔄 대화 초기화" 버튼 클릭

## 4️⃣ 학습 팁

### 초급 단계
- ✅ 변수, if문, 반복문부터 시작
- ✅ 각 문법을 '왜' 써야 하는지 질문하기
- ✅ 예제 코드를 직접 수정해보며 학습

### 중급 단계
- ✅ class vs struct 판단 기준 명확히 하기
- ✅ public/private 기계식 판단 연습
- ✅ 상속 도입 시점 조건 이해하기

### 효과적인 질문 방법
1. **구체적으로 질문**: "상속이 뭐야?" ❌ → "Player와 Enemy에 공통 코드가 3개 있는데 상속을 써야 할까?" ✅
2. **코드와 함께 질문**: 작성한 코드를 붙여넣고 리뷰 요청
3. **규칙 기반 질문**: "이 경우 4단 질문 중 어떤 게 YES인가요?"

## 5️⃣ 문제 해결

### "API 키 없음" 오류
- `config.ini` 파일이 있는지 확인
- API 키가 올바르게 입력되었는지 확인
- `src/` 폴더가 아닌 프로젝트 루트에 `config.ini` 위치 확인

### "오류 발생" 메시지
- 인터넷 연결 확인
- API 사용량 한도 확인 (Free tier는 일일 제한 있음)
- API 키가 유효한지 확인

### 프로그램이 느림
- Claude API 응답 대기 시간 (보통 3-10초)
- 백그라운드 처리로 UI는 멈추지 않음
- 복잡한 질문은 더 오래 걸릴 수 있음

## 6️⃣ exe 파일로 배포하기

```bash
# Windows
build.bat

# Linux/Mac
./build.sh
```

생성된 파일 위치: `src/dist/CPP_Learning_Tool.exe`

**주의**: exe 파일에도 `config.ini`가 필요합니다!
- exe 파일과 같은 폴더에 `config.ini` 복사
- 또는 환경변수로 `CLAUDE_API_KEY` 설정

---

## 🎯 8월까지 게임 완성 로드맵

1. **3월**: 초급 완료 (변수, if, 함수, struct)
2. **4월**: 초급후반 완료 (vector, switch, 배열)
3. **5월**: 중급초반 완료 (class, 생성자, 인벤토리)
4. **6월**: 중급 완료 (상속, virtual, 전투 시스템)
5. **7월**: 중급후반 완료 (스킬, 상태 패턴, 던전 게임)
6. **8월**: 최종 게임 통합 및 출시!

화이팅! 🚀

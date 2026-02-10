# C++ 게임 개발 실전 학습 도구

Claude API를 활용한 로컬 C++ 학습 프로그램입니다.

## 특징

- ✅ **로컬 실행**: API 키를 사용하여 로컬 환경에서 Claude와 대화
- ✅ **체계적 학습**: 초급부터 중급후반까지 단계별 연습 문제 제공
- ✅ **실전 중심**: 게임 개발을 목표로 한 실용적 문법 학습
- ✅ **규칙 기반**: '감각'이 아닌 '조건'으로 문법 사용 여부 판단
- ✅ **PyQt6 GUI**: 직관적인 사용자 인터페이스

## 설치 방법

### 1. Python 설치 확인
Python 3.8 이상이 필요합니다.

```bash
python --version
```

### 2. 저장소 클론
```bash
git clone https://github.com/fightspirit67-prog/my-cppagent.git
cd my-cppagent
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. API 키 설정 ⚠️ 중요!
다음 중 하나의 방법으로 API 키를 설정하세요:

#### 방법 1: config.ini 파일 사용 (권장)
```bash
# config.ini.example을 복사
cp config.ini.example config.ini

# config.ini 파일을 열어서 API 키 입력
# CLAUDE_API_KEY=sk-ant-api03-... 형식으로 입력
```

#### 방법 2: 환경변수 사용
```bash
# Windows (PowerShell)
$env:CLAUDE_API_KEY="your-api-key-here"

# Linux/Mac
export CLAUDE_API_KEY="your-api-key-here"
```

### 5. 프로그램 실행
```bash
cd src
python main.py
```

## 사용 방법

1. **프로그램 실행**: `src/main.py` 실행
2. **연습 문제 선택**: 왼쪽 사이드바에서 난이도별 문제 클릭
3. **자유 질문**: 하단 입력창에 C++ 관련 질문 입력
4. **대화 초기화**: 새로운 주제로 시작하려면 "대화 초기화" 버튼 클릭

## exe 파일 빌드

### PyInstaller로 실행 파일 생성

```bash
cd src
pyinstaller --onefile --windowed --name "CPP_Learning_Tool" main.py
```

생성된 exe 파일은 `dist/` 폴더에 위치합니다.

## 프로젝트 구조

```
webapp/
├── src/
│   ├── main.py              # 메인 애플리케이션
│   ├── claude_api.py        # Claude API 통신 모듈
│   └── exercise_manager.py  # 연습 문제 관리
├── data/
│   ├── cpp_rules.txt        # C++ 규칙 시스템 프롬프트
│   └── exercises.json       # 난이도별 연습 문제
├── requirements.txt         # Python 의존성
└── README.md               # 이 파일
```

## 난이도별 학습 내용

- **초급**: 변수, 입출력, if문, 반복문, 함수 기초
- **초급후반**: struct, 배열/vector, switch문
- **중급초반**: class, public/private, 생성자, 인벤토리 시스템
- **중급**: 상속, virtual, map, 전투 시스템
- **중급후반**: 스킬 시스템, 상태 패턴, 던전 게임 통합

## API 키 변경

**보안을 위해 API 키는 절대 코드에 직접 입력하지 마세요!**

### 방법 1: config.ini 파일 (권장)
1. `config.ini.example`을 `config.ini`로 복사
2. `config.ini` 파일 열기
3. `CLAUDE_API_KEY=your-api-key-here` 부분에 실제 API 키 입력
4. 저장 후 프로그램 실행

### 방법 2: 환경변수
```bash
# Windows
set CLAUDE_API_KEY=your-api-key-here

# Linux/Mac
export CLAUDE_API_KEY=your-api-key-here
```

**⚠️ 주의**: `config.ini` 파일은 `.gitignore`에 포함되어 있어 Git에 커밋되지 않습니다.

## 주의사항

- Claude API 사용량에 따라 비용이 발생할 수 있습니다.
- Free tier는 일일 사용량 제한이 있습니다.
- 인터넷 연결이 필요합니다.

## 라이선스

MIT License

# Necro-Circus [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Flimdev59%2FNecro-Circus&count_bg=%2379C83D&title_bg=%23555555&icon=counter-strike.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
![](README/circus.jpg)

#### 2D Game Programing Project  

<br><br>

---

<br><br>

- # Concept
  긴 잠에 들었던 이들과 펼치는 최고의 서커스  

<br><br>

---

<br><br>

- # Project Intention
  테라리아와 언더테일을 비롯한 여러 게임들은 내게 잊을 수 없는 추억을 선사하며, 깊은 영감을 남겼습니다.  
  어린 시절, 어둠 속 두려움의 상징이었던 괴물들이 가장 찬란한 이야기를 품어낼 때의 그 감동처럼,  
  이제 나 또한 그 길을 함께 걸어갈 어린 이들에게 순수함과 기쁨, 그리고 가슴을 울리는 따뜻한 추억을 남기고자 이 게임을 만들것입니다. 

<br><br>

---

<br><br>

- # Material & Genre
  언데드 & 몬스터를 소재로한 횡스크롤 액션 플랫포머 시뮬레이션 어드벤처 게임  

<br><br>

---

<br><br>

- # Key Platforms (System Specifications)

<br>   

  | 구분           | 최소 사양                         | 권장 사양                         |
  |----------------|-----------------------------------|-----------------------------------|
  | **Windows**    |                                   |                                   |
  | 운영체제       | Windows 7 이상                   | Windows 7 이상                   |
  | 프로세서       | 2.0GHz CPU                       | 3.0GHz 이상의 듀얼코어 CPU       |
  | 메모리         | 2.5GB                            | 4GB                               |
  | 그래픽 카드    | 128MB 비디오 메모리             | 256MB 비디오 메모리             |
  |                | 2.0 이상의 셰이더 모델           | 2.0 이상의 셰이더 모델           |
  | API            | DirectX 9.0c 이상                | DirectX 9.0c 이상                |
  | 저장 공간      | 200MB                            | 200MB                             |
  | **macOS**      |                                   |                                   |
  | 운영체제       | OS X 10.9.5 - 10.11.6           | OS X 10.9.5 - 10.11.6           |
  | 프로세서       | 2.0GHz CPU                       | 3.0GHz 이상의 듀얼코어 CPU       |
  | 메모리         | 2.5GB                            | 4GB                               |
  | 그래픽 카드    | 128MB 비디오 메모리             | 256MB 비디오 메모리             |
  |                | OpenGL 3.0 이상 지원            | OpenGL 3.0 이상 지원            |
  | 저장 공간      | 200MB                            | 200MB                             |

<br>   

<br><br>

- # User Target Range
  전체이용가로 모두가 즐길 수 있다

<br><br>

---

<br><br>

- # Differences from other games
  스토리 진행이나 스테이지 넘어갈때 버려지는 요소가 많아 재사용되는 리소스를 활용하되 차별을 두어
  다른 기믹과 디자인을 일부 추가해 플레이어가 지루할 요소를 줄이고 즐길 요소를 늘린다

<br><br>

---

<br><br>

- # *Main Story*
  ### Prolog
  주인공은 죽음을 맞이하지만, 뛰어난 엔터테인먼트 능력을 눈여겨본 사신은 새로운 임무를 부여하기로 한다.
  그는 죽은 후 해골 엔터테이너로 변하며 본인의 이름 외에는 모든 기억이 지워진다.
  
  사신이 부여한 임무는 한 서커스단의 재건, 주인공을 폐허가 된 서커스에 이유에
  주인공은 폐허가 된 서커스 옆 공동묘지에서 영문도 모른 채 깨어나 해골들과의 전투를 통해 튜토리얼을 진행한다.
  전투 후, 그는 해골들과 협상하여 충분한 보수를 약속하고 그들을 고용함으로써 서커스를 재건하기 시작한다.
  
  주인공은 새롭게 만든 서커스의 이름을 "네크로 서커스"로 정하고, 게임의 이야기는 여기서부터 시작된다.

 <br><br>

---
<br><br>

- # Game Composition

### 예상 게임 실행 흐름

1. **시작 화면**
   - 로고와 제목이 표시되며, 시작 버튼과 옵션 버튼이 있다.

2. **로비**
   - 퀘스트 목록 확인 (할 일 확인)
   - 탐험 버튼 클릭 → 월드맵 화면으로 전환
   - 구성 버튼 클릭 → 괴물 고용 및 공연 구성 화면으로 전환
   - 공연 버튼 클릭 → 공연 실행 및 전투 화면으로 전환
   - NPC와 상호작용 가능 (좌우 화살표로 이동)

3. **탐험 화면**
   - 새로운 지역 탐험 선택
   - 전투 또는 보상 화면으로 전환
   ![](README/map.png)

4. **구성 화면**
   - 고용한 괴물 선택 및 공연 구성
   - 보상 및 조건 확인 후 공연 설정

5. **전투 화면**
   - 공연 구성에 따라 적들과 전투
   - 성공 시 보상 획득 및 서커스 성장

6. **결과 화면**
   - 전투 결과 및 보상 표시
   - 로비로 돌아가기 또는 재탐험 선택

<br><br>  

---  

<br><br>

- # Scene type and configuration & switching rules

### Scene 종류 및 구성, 전환 규칙

1. **로비 Scene**
   - 게임의 중앙 허브. 퀘스트, 탐험, 구성, 공연 버튼 포함.

2. **탐험 Scene**
   - 월드맵 탐험 및 적 발견 화면.
   - 전투 Scene으로 전환 시: 선택한 지역에서 적 등장.

3. **구성 Scene**
   - 고용한 괴물 선택 및 공연 구성.
   - 공연 Scene으로 전환 시: 선택된 괴물과 관련된 전투.

4. **전투 Scene**
   - 공연 및 전투가 진행되는 곳.
   - 결과에 따라 로비로 돌아가거나 탐험 진행.

<br><br>  

---  

<br><br>  

### GameObject 종류 및 상호작용

- **주인공**
  - 플레이어 캐릭터, 스킬 사용 및 적과의 전투.
  
- **적 (해골, 좀비 등)**
  - 전투에서 상대하는 대상, 각기 다른 능력 보유.
  
- **NPC**
  - 퀘스트 제공, 거래 가능.
  
- **버튼 (UI)**
  - 각 Scene 간 전환 및 상호작용을 위한 요소.
  
- **아이템**
  - 보상 및 업그레이드에 사용될 아이템.

<br><br>  

---  

<br><br>  

### 각 클래스 역할 및 생김새 설명

- **Player**
  - 주인공 캐릭터, 스킬 및 능력 처리.

- **Enemy**
  - 적 캐릭터, AI 및 전투 로직.

- **SceneManager**
  - 각 Scene 전환 및 관리.

- **QuestManager**
  - 퀘스트 진행 및 상태 관리.

- **BattleSystem**
  - 전투 로직 및 전투 진행.

- **UIManager**
  - 사용자 인터페이스 및 HUD 관리.

<br><br>  

---  

<br><br>  

### 화면에 보이지 않는 Controller 객체들

- **InputController**
  - 사용자 입력 관리 및 이벤트 처리.

- **AudioController**
  - 음악 및 효과음 관리.

- **DataController**
  - 게임 데이터 저장 및 로드.

<br><br>  

---  

<br><br>  

### 개발 기법 소개

- **싱글톤 패턴**
  - 싱글톤 코어 객체를 통한 쉬운 관리.

- **객체 지향 프로그래밍 (OOP)**
  - 각 클래스 간의 역할 분담 및 상호작용을 통한 구조화.

- **상태 머신 패턴**
  - 주인공 및 적의 상태 전환 관리.

- **이벤트 기반 프로그래밍**
  - 사용자 입력 및 게임 내 이벤트 처리.

<br><br>  

---  

<br><br>  

### 게임 프레임워크 기능

- **장면 관리**
  - 여러 Scene 간 전환 및 데이터 공유.

- **자원 관리**
  - 이미지, 사운드, 애니메이션 관리.

- **물리 엔진**
  - 물리적 상호작용 처리 (적 충돌 및 이동).
  
<br><br>  

---  

<br><br>  

### 일정

- **10/28 이전 준비 사항**
  - 게임 기획서 완성
  - 각 Scene 및 GameObject 정의

- **10/28부터 7주간 개발 계획**
  - 1주차: 프레임워크 개발
  - 2주차: 탐험 필드 및 전투 시스템 구현
  - 3주차: 괴물 고용 및 구성 시스템 구현
  - 4주차: 퀘스트 시스템 구현
  - 5주차: 최종 전투 및 결과 화면 구현
  - 6주차: 디버깅 및 밸런스 조정
  - 7주차: 최종 테스트 및 배포 준비

<br><br>  

### 1~3주차 개발 진행 요약
최근 커밋(3일 전)된 파일들:

Manager (framework commit 2)
Object (framework commit 2)
Scene (framework commit 2)
CCore.py (framework commit 2)
Sprite.py (framework commit 2)
CScene.py (framework commit 2)
Constants.py (framework commit 2)
지난주 커밋된 파일들:

UI (framework commit)
Config.py (framework commit)
GameData.py (framework commit)
Utility.py (framework commit)
커밋 날짜가 명시되지 않은 파일:

main.py (커밋 정보 없음)

싱글톤패턴의 프레임워크를 개발함, 직접 도트를 찍어 배경과 스프라이트 이미지를 만듬  

![](README/skeleton_large_after.png)  
![](README/girl.png)  
![](README/backgrounds1.png)  
![](README/backgrounds2.png)  
![](README/backgrounds3.png)  
![](README/backgrounds4.png)  
![](README/backgrounds5.png)  


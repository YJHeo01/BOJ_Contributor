# BOJ_STAT V2

[![BOJ](https://bojstat.vulcan.site/v2/en/sk14cj?v=4)](https://www.acmicpc.net/user/sk14cj)
[![BOJ](https://bojstat.vulcan.site/v2/ko/sk14cj?v=3)](https://www.acmicpc.net/user/sk14cj)

## 📖 사용법

---
```bash
# 사용 방법

# 영어 ver
[![BOJ](https://bojstat.vulcan.site/v2/en/sk14cj)](https://www.acmicpc.net/user/sk14cj)

# 한글 ver
[![BOJ](https://bojstat.vulcan.site/v2/ko/sk14cj)](https://www.acmicpc.net/user/sk14cj)

위 URL에서 sk14cj를 제거하고, 본인의 핸들을 작성한 후 GitHub README 파일에 삽입하면 됩니다.

# 커스텀 기능 (추가 예정)
- 쿼리 파라미터를 사용하지 않을 경우 각각 제목:, 내용:, 배경: 과 같은 색상이 적용됩니다.
- 쿼리 파라미터를 활용하여, 제목, 내용, 배경 색을 변경하여 나만의 뱃지를 만들 수 있습니다!
- ex) 언어 : 한글, 보라색 제목, 검은 내용, 하얀 배경을 사용하고 싶은 경우 (우측 뱃지)
- [![BOJ](https://bojstat.vulcan.site/v2/ko/sk14cj)](https://www.acmicpc.net/user/sk14cj)
- Codeforces 혹은 AtCoder 핸들과 뱃지 제목의 색상을 맞추고, 어울리는 배경 및 내용 색상을 찾아보세요!
- 본인의 Solved.ac 티어 이미지와 어울리는 색깔 조합을 찾아보세요!
- 쿼리 파라미터로는 색상을 대표하는 키워드, RGB값을 모두 사용하실 수 있습니다.
- 키워드 :
- Solved.ac 컬러 RGB 값 : 다이아몬드(#00B4FC), 플래티넘(#27E2A4), 골드(#EC9A00), 실버(#435F7A), 브론즈(#AD5600)


```

---

## 🚀 주요 기능

- 백준 온라인 저지 생태계 기여도 및 백준 활동을 보여주는 Github 뱃지입니다.
- 쿼리 파라미터를 활용하여 유저가 원하는 색상 조합을 사용할 수 있습니다. (추가 예정)
- 자세한 사용법은 상단에 있는 사용법-커스텀 기능 카테고리를 참고해주세요.
- 만든 문제(Authored Problems) : 해당 유저가 만든 문제를 뜻합니다.
- 검수한 문제(Reviewed Problems) : 해당 유저가 검수한 문제를 뜻합니다.
- 공헌한 문제(Fixed Problems) : 데이터 추가, 오타 수정 등의 기여로 완성도를 높인 문제를 뜻합니다.
- 난이도 기여(Rating Contributions) : solved.ac에서의 난이도 기여를 뜻합니다.
- 기록은 하루에 최대 한번 업데이트 됩니다.


---

# BOJ_STAT V1 (BOJ_Contributor)

[![BOJ](https://bojstat.vulcan.site/user/sk14cj?v=3)](https://www.acmicpc.net/user/sk14cj)

## 📖 사용법

---
```bash
# 실행 방법

[![BOJ](https://bojstat.vulcan.site/user/sk14cj)](https://www.acmicpc.net/user/sk14cj)

혹은

[![BOJ](https://bojstat.vulcan.site/sk14cj)](https://www.acmicpc.net/user/sk14cj) (<-새로 올린 버전)

위 URL에서 sk14cj를 제거하고, 본인의 핸들을 작성한 후 GitHub README 파일에 삽입하면 됩니다.

문제가 있을 경우 레포지토리에 이슈를 생성해주시거나, https://www.acmicpc.net/board/view/158187에 댓글을 남겨주세요.

```

---

## 📌 개발 의도

문득, PS 생태계 기여도를 보여주는 뱃지를 만들어 볼 생각이 들었습니다.

​대다수 깃헙 PS 뱃지들은 문제를 얼마나 풀었는가에 초점을 맞추지, PS 생태계에 얼마나 기여했는지 보여주는 뱃지를 본 기억은 없기 때문입니다.

그래서, 백준 온라인 저지 문제에 기여(문제 출제, 문제 검수 등) 한 정도를 나타내는 뱃지를 만들면 좋겠다는 생각을 하였습니다.

​Problem Solving을 즐기는 한 사람으로서, PS 생태계에 기여한 모든 분들께 감사의 인사를 전하며 프로그램을 만들어 보고자 합니다.

---

## 🚀 주요 기능

- 백준 온라인 저지 생태계 기여도를 보여주는 GitHub 뱃지입니다.
- 만든 문제 : 해당 유저가 만든 문제를 뜻합니다.
- 검수한 문제 : 해당 유저가 검수한 문제를 뜻합니다.
- 공헌한 문제 : 데이터 추가, 오타 수정 등의 기여로 완성도를 높인 문제를 뜻합니다.
- 난이도 기여 : solved.ac에서의 난이도 기여를 뜻합니다.
- 기록은 하루에 최대 한번 업데이트 됩니다.


---

## 🛠️ 기술 스택

- Python
- Flask

---

## 📂 프로그램 구조

```
BOJ_Contributor
│   README.md
│   app.py
│   user_data.db
└───api
    │   main.py
    │   boj_user_page.py
    │   solved_user_page.py
└───badge_generator
    │   v1_badge.py
    │   v2_badge_ko.py
    │   v2_badge_en.py
└───tier_image
    │   solved.ac 티어 PNG 이미지 31개
```

---


## ✨ 향후 계획

- 뱃지 디자인 추가 (현재 작업 중)
- 뱃지 디자인 관련 기여 모두 환영합니다!

---

## 📄 도움을 주신 분

서버 제공 : [vulcan](https://github.com/firekann)님<br>
티어 이미지 제공 : [Solved.ac](https://solved.ac/)

---

## 📞 문의

- 당일 기록이 업데이트가 되지 않은 상황에서 프로그램에 요청이 올 경우, 백준 온라인 저지의 웹페이지를 읽는 방식이라 백준 서버에 큰 부담이 되지 않을거라 판단해서 프로그램을 제작했지만, 혹여나 이 프로그램이 문제가 될 경우 하단 연락처로 연락을 주시면 프로그램을 중단하도록 하겠습니다.
- 그 외에도 문의사항이 있을 경우, 이슈에 글을 남겨주시거나, 하단 연락처로 연락해주시길 바랍니다.
- https://github.com/YJHeo01/BOJ_Contributor/issues
- https://www.acmicpc.net/board/view/158187
- sk14cj@inu.ac.kr

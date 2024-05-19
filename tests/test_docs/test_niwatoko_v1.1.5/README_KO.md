韓国語への翻訳:

# niwatoko v1.1.5
# niwatoko v1.1.5

프로그래밍 언어 Niwatoko에서는 모듈 가져오기 기능(세계 최초*)을 제공하기 시작했습니다.
Anthropic의 프롬프트 생성기가 생성한 변수가 포함된 Markdown 파일을 Niwatoko에서 처리할 수 있게 되었습니다.

## 업데이트 내용

### 가져오기(인용) 기능 추가
- Markdown 파일 내에서 다른 파일의 내용을 인용할 수 있게 되었습니다.
- 이를 통해 코드의 재사용성이 향상되고 문서 관리가 용이해졌습니다.

- 인용 방법은 다음과 같습니다:
   ```markdown
   - `변수명` = 확장자 [./파일경로(확장자 제외)]
   - `변수명` = [./파일경로]
   ```
- 예:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- 이 기능은 세계 최초의 시도입니다.
- 파일 확장자(.py)는 대괄호[]에 포함해야 합니다.

### 문서 변수 기능 추가
- Markdown 파일 내에서 {{변수}}를 정의하고, 해당 {{변수}}를 다른 곳에서 참조할 수 있게 되었습니다.
  - 예를 들어, `{{변수명}}`이라고 쓰면 같은 디렉토리의 `변수명.md` 파일이 읽혀집니다.
- 이를 통해 문서의 가독성과 유지보수성이 향상됩니다.

## 설치

자세한 내용은 다음 URL을 참고하세요:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)

1. Python이나 Anthropic 키 등이 이미 설정된 경우 다음 명령어로 사용할 수 있습니다:

   ```
   pip install niwatoko
   ```

   또는 최신 버전으로 업그레이드하려면 다음 명령어를 실행하세요:

   ```
   pip install --upgrade niwatoko
   ```

## 연습 문제

다음 단계를 따라 진행하세요:

- 준비
1. 이 리포지토리의 main 브랜치를 클론합니다.

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. 클론한 디렉토리로 이동합니다.

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- 실행
1. `test_input.md` 파일을 준비합니다. 이 파일에는 테스트할 입력 내용이 기술되어 있습니다.

```test_input.md
## 인용
- `addition_py` = py [./test_import_module_add]
```py
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
```

## TODO
`addition_py` 와 `multiplication_py`를 한국어로만 요구사항 명세서로 변환하세요.
또한 필요한 테스트도 기술하세요.
```

2. 다음 명령어를 실행하여 `test_input.md`의 내용을 변환하고 `output.md` 파일에 출력합니다:

   ```
   niwatoko test_input.md -o output.md
   ```

3. 다음 명령어를 실행하여 `output.md`의 내용을 Python 코드로 변환하고 `output.py` 파일에 출력합니다:

   ```
   niwatoko output.md -o output.py
   ```

4. 생성된 `output.md`와 `output.py` 파일의 내용을 확인하고 출력이 예상대로 되었는지 확인합니다.

5. 예상대로 출력되지 않으면 반복해서 실행합니다.
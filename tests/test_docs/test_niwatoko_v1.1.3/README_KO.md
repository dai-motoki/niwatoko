韓国語への翻訳:

# niwatoko v1.1.3

私たちは、Anthropicのドキュメント変数機能をオープンソース(世界で2番目*)として再現し、モジュールインポート機能(世界初*)を提供しました。

## 업데이트 내용

### 인용(Import) 기능 추가
- Markdown 파일 내에서 다른 파일의 내용을 인용할 수 있게 되었습니다.
- 이를 통해 코드의 재사용성이 향상되고 문서 관리가 용이해집니다.

- 인용 방법은 다음과 같습니다:
   ```markdown
   - `변수명` = 확장자 [./파일경로(확장자명 제외)]
   - `변수명` = [./파일경로]
   ```
- 예:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- 이 기능은 세계 최초의 시도입니다.
- 파일 확장자(.py)는 대괄호[]안에 포함해야 한다는 점에 유의하세요.

### 문서 변수 기능 추가
- Markdown 파일 내에서 변수를 정의하고 다른 곳에서 참조할 수 있게 되었습니다.
- 이를 통해 문서의 가독성과 유지보수성이 향상됩니다.
- 이 기능은 Anthropic에 이어 세계에서 두 번째로 구현된 것입니다.

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
def add(a, b):
    """
    두 숫자를 더하는 함수

    Parameters:
    a (int or float): 첫 번째 숫자
    b (int or float): 두 번째 숫자

    Returns:
    int or float: a와 b의 합
    """
    return a + b

def add_list(numbers):
    """
    숫자 리스트의 합을 계산하는 함수

    Parameters:
    numbers (list): 숫자 리스트

    Returns:
    int or float: 숫자들의 합
    """
    total = 0
    for num in numbers:
        total = add(total, num)
    return total

def add_multiple(*args):
    """
    여러 숫자를 더하는 함수

    Parameters:
    *args: 가변 길이 인수. 임의의 숫자 값을 받습니다.

    Returns:
    int or float: 전달된 인수들의 합
    """
    return add_list(args)
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
def multiply(a, b):
    """
    두 숫자를 곱하는 함수

    Parameters:
    a (int or float): 첫 번째 숫자
    b (int or float): 두 번째 숫자

    Returns:
    int or float: a와 b의 곱
    """
    return a * b

def multiply_list(numbers):
    """
    숫자 리스트의 곱을 계산하는 함수

    Parameters:
    numbers (list): 숫자 리스트

    Returns:
    int or float: 숫자들의 곱
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total


def multiply_multiple(*args):
    """
    여러 숫자를 곱하는 함수

    Parameters:
    *args: 가변 길이 인수. 임의의 숫자 값을 받습니다.

    Returns:
    int or float: 전달된 인수들의 곱
    """
    return multiply_list(args)```

## TODO
`addition_py`와 `multiplication_py`를 한국어로 요구사항 명세서로 변환하세요.
또한 필요한 테스트 케이스도 작성하세요.
```

2. 다음 명령어를 실행하여 `test_input.md`의 내용을 변환하고 `output.md` 파일에 출력합니다:

   ```
   niwatoko test_input.md -o output.md
   ```

3. 다음 명령어를 실행하여 `output.md`의 내용을 Python 코드로 변환하고 `output.py` 파일에 출력합니다:

   ```
   niwatoko output.md -o output.py
   ```

4. 생성된 `output.md`와 `output.py` 파일의 내용을 확인하고 출력이 예상대로 이루어졌는지 확인합니다.

5. 예상대로 출력되지 않으면 반복하여 실행합니다.
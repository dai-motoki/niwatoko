هذا هو الترجمة إلى اللغة العربية:

# niwatoko v1.1.3

لقد قمنا بإعادة إنتاج ميزة متغيرات المستند التابعة لـ Anthropic كمصدر مفتوح (الثاني في العالم*) ، وقدمنا ميزة استيراد الوحدات (الأولى في العالم*).

## محتويات التحديث

### إضافة ميزة الاستيراد (الاقتباس)
- أصبح من الممكن الآن اقتباس محتوى ملفات أخرى داخل ملفات Markdown.
- سيؤدي هذا إلى تحسين إعادة استخدام الرمز وتسهيل إدارة المستندات.

- طريقة الاقتباس هي كما يلي:
   ```markdown
   - `اسم_المتغير` = امتداد [./مسار_الملف(بدون امتداد)]
   - `اسم_المتغير` = [./مسار_الملف]
   ```
- مثال:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- هذه الميزة هي محاولة أولى من نوعها في العالم.
- لاحظ أن امتداد الملف (.py) يجب أن يكون داخل الأقواس المربعة [].

### إضافة ميزة متغيرات المستند
- أصبح من الممكن تعريف المتغيرات داخل ملفات Markdown والإشارة إليها في أماكن أخرى.
- سيؤدي هذا إلى تحسين قابلية قراءة المستند والحفاظ عليه.
- هذه الميزة هي الثانية في العالم بعد Anthropic.

## التثبيت

للمزيد من التفاصيل، يرجى زيارة الرابط التالي:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)


1. بالنسبة للأشخاص الذين لديهم Python وأي مفاتيح Anthropic مُعدة مسبقًا، يمكنهم استخدام الأمر التالي:

   ```
   pip install niwatoko
   ```

   أو لترقية إلى أحدث إصدار، قم بتنفيذ الأمر التالي:
   
   ```
   pip install --upgrade niwatoko
   ```


## تمارين

يرجى اتباع الخطوات التالية:
- الإعداد
1. استنسخ فرع main من هذا المستودع.

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. انتقل إلى الدليل المنسوخ.

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- التنفيذ

1. أعد إنشاء ملف `test_input.md`. هذا الملف يحتوي على محتوى الإدخال الذي تريد اختباره.

```test_input.md
## الاقتباس
- `addition_py` = py [./test_import_module_add]
```py
def add(a, b):
    """
    Function to add two numbers

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: Sum of a and b
    """
    return a + b

def add_list(numbers):
    """
    Function to calculate the sum of a list of numbers

    Parameters:
    numbers (list): List of numbers

    Returns:
    int or float: Sum of numbers
    """
    total = 0
    for num in numbers:
        total = add(total, num)
    return total

def add_multiple(*args):
    """
    Function to add multiple numbers

    Parameters:
    *args: Variable-length arguments. Accepts any number of numeric values

    Returns:
    int or float: Sum of the passed arguments
    """
    return add_list(args)
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
def multiply(a, b):
    """
    Function to multiply two numbers

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: Product of a and b
    """
    return a * b

def multiply_list(numbers):
    """
    Function to calculate the product of a list of numbers

    Parameters:
    numbers (list): List of numbers

    Returns:
    int or float: Product of numbers
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total


def multiply_multiple(*args):
    """
    Function to multiply multiple numbers

    Parameters:
    *args: Variable-length arguments. Accepts any number of numeric values

    Returns:
    int or float: Product of the passed arguments
    """
    return multiply_list(args)```

## TODO
قم بتحويل `addition_py` و `multiplication_py` إلى مواصفات متطلبات باللغة اليابانية فقط.
كما قم بتضمين الاختبارات اللازمة.
```

2. قم بتنفيذ الأمر التالي لتحويل محتوى `test_input.md` وإخراجه إلى ملف `output.md`:

   ```
   niwatoko test_input.md -o output.md
   ```

3. قم بتنفيذ الأمر التالي لتحويل محتوى `output.md` إلى كود Python وإخراجه إلى ملف `output.py`:

   ```
   niwatoko output.md -o output.py
   ```

4. تحقق من محتوى الملفين `output.md` و `output.py` المنشأين والتأكد من أن الإخراج كما هو متوقع.

5. كرر الخطوات السابقة حتى تحصل على الإخراج المتوقع.
def factorial(n):
    """计算n的阶乘
    
    Args:
        n: 一个非负整数
        
    Returns:
        n的阶乘
        
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """返回斐波那契数列的第n项
    
    Args:
        n: 一个非负整数
        
    Returns:
        斐波那契数列的第n项
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def is_palindrome(text):
    """检查字符串是否为回文
    
    Args:
        text: 输入字符串
        
    Returns:
        如果是回文，返回True；否则返回False
    """
    text = text.lower()
    return text == text[::-1]

def count_words(sentence):
    """计算句子中的单词数
    
    Args:
        sentence: 输入的句子
        
    Returns:
        单词数量
    """
    words = sentence.split()
    return len(words)

def is_prime(n):
    """判断一个数是否为素数
    
    Args:
        n: 一个大于1的整数
        
    Returns:
        如果是素数，返回True；否则返回False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

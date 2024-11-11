def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    return 7 // 2


def float_multiplication():
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    return 3.0 * 2


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    return (float_multiplication() + int_division())


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    words_list = "Python is awesome!".split()
    extracted = words_list[2].removesuffix("!")
    
    return extracted
    
    


def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    to_lower = 'Python is awesome!'
    
    return to_lower.lower()


def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    count = 0
    thisString = 'Python is awesome!'
    
    for letter in thisString:
        if letter == "o":
            count += 1
            
    return count


def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    return (not (5 > 3) and (10 == 5 * 2))

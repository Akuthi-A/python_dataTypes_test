def add_to_list(numbers):
    """
    Task:
    - Add the number 6 to the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers.append(6)
    return numbers


def remove_from_list(numbers):
    """
    Task:
    - Remove the number 3 from the given list `numbers`.
    
    Return:
    - The modified list.
    """
    if 3 in numbers:
        numbers.remove(3)
    else:
        print("Number is not in list")
    return numbers


def insert_at_beginning(numbers):
    """
    Task:
    - Insert the number 0 at the beginning of the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers = [0] + numbers
    return numbers


def reverse_list(numbers):
    """
    Task:
    - Reverse the order of elements in the list `numbers`.
    
    Return:
    - The reversed list.
    """
    return numbers[::-1]


def create_new_tuple(t):
    """
    Task:
    - Create a new tuple that contains the first two elements of the tuple `t`.
    
    Return:
    - The new tuple with the first two elements.
    """
    return (t[0], t[1])


def check_if_value_exists(t, value):
    """
    Task:
    - Check if the value 15 exists in the tuple `t`.
    
    Return:
    - True if the value exists, otherwise False.
    """
    if value in t:
        return True
    else:
        return False


def find_intersection(set1, set2):
    """
    Task:
    - Find the intersection of sets `set1` and `set2`.
    
    Return:
    - The intersection of the two sets.
    """
    intersect = []
    
    for item in set1:
        if item in set2:
            intersect.append(item)

    return set(intersect)


def find_union(set1, set2):
    """
    Task:
    - Find the union of sets `set1` and `set2`.
    
    Return:
    - The union of the two sets.
    """
    union = list(set1) + list(set2)
    
    return set(union)


def find_difference(set1, set2):
    """
    Task:
    - Find the difference between set1 and set2 (i.e., set1 - set2).
    
    Return:
    - The difference between the two sets.
    """
    difference = []
    
    for item in set1:
        if item not in set2:
            difference.append(item)

    return set(difference)


def add_student(student_grades):
    """
    Task:
    - Add a new student 'David' with a grade of 92 to the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with the new student.
    """
    student_grades['David'] = 92
    
    return student_grades


def change_bob_grade(student_grades):
    """
    Task:
    - Change Bob’s grade to 95 in the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with Bob’s grade changed.
    """
    student_grades['Bob'] = 95
    
    return student_grades


def delete_charlie(student_grades):
    """
    Task:
    - Delete 'Charlie' from the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with Charlie removed.
    """
    del student_grades['Charlie']
    
    return student_grades


def retrieve_alice_grade(student_grades):
    """
    Task:
    - Retrieve the grade of Alice from the dictionary `student_grades`.
    
    Return:
    - Alice's grade.
    """
    return student_grades['Alice']

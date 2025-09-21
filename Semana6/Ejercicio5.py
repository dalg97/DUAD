def upper_lower(word):
    upper_count = 0
    lower_count = 0
    for letter in word:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
        else:
            continue
    print(f"There are {upper_count} upper letter and {lower_count} lower letters")

upper_lower("Diego is a System Engineer")


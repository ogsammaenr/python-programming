def balanced_brackets(my_string: str):
    brackets = "".join([char for char in my_string if char in "()[]"])

    if len(brackets) == 0:
        return True

    if not (
        (brackets[0] == "(" and brackets[-1] == ")")
        or (brackets[0] == "[" and brackets[-1] == "]")
    ):
        return False

    # remove first and last character
    return balanced_brackets(brackets[1:-1])


# Test Alanı
if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)

    # Çıktı:
    #
    # True
    # True
    # False
    # False

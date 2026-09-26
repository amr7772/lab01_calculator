# -*- coding: utf-8 -*-
"""lab01

Original file is located at
    https://colab.research.google.com/drive/114y5GKP3enMi09rwO6k_zQO6xaKxwcHx
"""

def letter_grade(mark):
    """Return the letter grade for a mark between 0 and 100."""
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100.")
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


def main():
    entry = input("Enter a mark out of 100: ").strip()

    try:
        mark = float(entry)
    except ValueError:
        print(f"Invalid input: '{entry}' is not a number.")
        return

    try:
        grade = letter_grade(mark)
    except ValueError as error:
        print(f"Invalid mark: {error}")
        return

    print(f"Mark: {mark:g}  ->  Grade: {grade}")


if __name__ == "__main__":
    main()

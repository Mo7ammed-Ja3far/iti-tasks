import re


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]

def merge_lists(lst1: list, lst2: list) -> list:
    return lst1 + lst2

def group_names_by_alpha(names: list[str]) -> dict[str, list[str]]:
    grouped_names = {}
    for name in sorted(names):
        if not name:
            continue
        first_letter = name[0].upper()
        grouped_names.setdefault(first_letter, []).append(name)
    return dict(sorted(grouped_names.items()))

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def get_user_info() -> dict[str, str]:
    while True:
        name = input("Enter your name: ").strip()
        if name and not name.isdigit():
            break
        print("Invalid name. Please enter a non-empty, non-numeric string.")

    while True:
        email = input("Enter your email: ").strip()
        if is_valid_email(email):
            break
        print("Invalid email format. Please try again.")

    return {"name": name, "email": email}

if __name__ == "__main__":
    print(is_palindrome("aabaa"))
    print(is_palindrome("abac"))
    print(is_palindrome("a"))
    print(merge_lists([1, 2, 3], [4, 5, 6]))
    sample_names = ["Ahmed", "Ali", "Bassem", "Amr", "Caren", "Badr"]
    print(group_names_by_alpha(sample_names))
    user_data = get_user_info()
    print(f"\nUser Data:\nName: {user_data['name']}\nEmail: {user_data['email']}")
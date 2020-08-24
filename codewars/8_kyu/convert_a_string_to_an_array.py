def string_to_array(s: str) -> list:
    """Return string as an array of words."""
    return list(s.split(" "))


def string_to_array_community(s: str) -> list:
    """Return string as an array of words."""
    return list(s.split()) if s else [""]


print(string_to_array("Hello world!"))
print(string_to_array(""))
print(string_to_array_community("Hello world!"))
print(string_to_array_community(""))

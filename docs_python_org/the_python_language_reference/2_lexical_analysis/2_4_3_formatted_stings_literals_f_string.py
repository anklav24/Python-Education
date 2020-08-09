"""
f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
replacement_field ::=  "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
f_expression      ::=  (conditional_expression | "*" or_expr)
                         ("," conditional_expression | "," "*" or_expr)* [","]
                       | yield_expression
conversion        ::=  "s" | "r" | "a"
format_spec       ::=  (literal_char | NULL | replacement_field)*
literal_char      ::=  <any code point except "{", "}" or NULL>
"""

a, b, c = 1, 200, 'string'
print(f"{a} plus {b} equal {a + b}")

# TRICKS
# To display both the expression text and its value after evaluation, (useful in debugging),
# an equal sing '=' may be added after the expression.
print(f"{a}")
print(f"{a=}")
print(f"{b =}")
print(f"{a + b=}")

print(f"{b:10}")
print(f"{a:10} and {10:10} 1234")
print(f"{a:05}")
print(f"{a:04}")
print(f"{a:x<3}")
print(f"{1.321324:.3}")  # Round
print(f"{1000000:,}")  # Separating thousands with commas

# Print curly braces

print(f"{a} within {{ and }}")
print(f"{{{{74}}}}")

# Printing datetimes

import datetime

today = datetime.datetime(year=2019, month=11, day=5)
print(f"{today:%B %d, %Y}")
print(f"{today:%d.%m.%y}")
print(f"{today:%Y-%m-%d}")

print(f"{c !s}")  # str()
print(f"{c !r}")  # repr()
print(f"{'йцукен' !a}")  # ascii()


# Многострочные F-Stings
name = 'Test'
profession = 'Tech'
affiliation = 123
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)

print(message)

message = f"""
Hi {name}. 
    You are a {profession}. 
  You were in {affiliation}.
"""

print(message)

age = 1
print(f"The \"comedian\" is {name}, aged {age}.")  # Экранирование кавычек

# To include a value in which a backslash escape is required, create a temporary variable.

newline = ord('\n')
print(f"newline: {newline}")
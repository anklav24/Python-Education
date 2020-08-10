"""
integer      ::=  decinteger | bininteger | octinteger | hexinteger
decinteger   ::=  nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
bininteger   ::=  "0" ("b" | "B") (["_"] bindigit)+
octinteger   ::=  "0" ("o" | "O") (["_"] octdigit)+
hexinteger   ::=  "0" ("x" | "X") (["_"] hexdigit)+
nonzerodigit ::=  "1"..."9"
digit        ::=  "0"..."9"
bindigit     ::=  "0" | "1"
octdigit     ::=  "0"..."7"
hexdigit     ::=  digit | "a"..."f" | "A"..."F"
"""
# There is no limit for the length of integer literals apart from what can be stored in available memory.
# Underscores are ignored for determining the numeric value of the literal. They can be used to group digits for enhanced readability. One underscore can occur between digits, and after base specifiers like 0x.
a = 1_000_000
b = 1000000
с = 0000_0000
d = 0000000
e = 0
print(a, b, с, d, e)

# Note that numeric literals do not include a sign; a phrase like -1 is actually an expression composed of the unary operator ‘-‘ and the literal 1.
# 100 This is an integer literal. 100
# -100 This is not a literal, but it's an expression. -100

# Some examples of floating point literals:
#
# 3.14    10.    .001    1e100    3.14e-10    0e0    3.14_15_93

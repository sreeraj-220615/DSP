import re
'''
#QUESTION_1
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
m = phoneRegex.search("My number is 415-555-4242")
print ("Group 0 (Full match):",m.group(0))
print ("Group 1 (Area code):",m.group(1))
print ("Group 2 (Phone number):",m.group(2))

#QUESTION_2

pattern = re.compile(r'https?://\S+')
text = "http://example.com https://google.com"

print(pattern.findall(text))

#QUESTION_3
regex = re.compile(r'(\d{1,4})[/-](\d{1,2})[/-](\d{1,4})')
def clean_date (match):
    a,b,c = match.groups()
    if len(a) ==4 :
        return f"{a}-{b.zfill(2)}-{c.zfill(2)}"
    else:
        return f"{a}-{b.zfill(2)}-{c.zfill(2)}"
text="3/14/2025,03-14-2015,2015/3/14"
print("Cleaned:",regex.sub(clean_date,text))

#QUESTION_4
pattern = re.compile(r'^\d{1,3}(,\d{3})*$')

nums = ["42", "1,234", "6,368,745", "12,34,567", "1234"]

for n in nums:
    if pattern.match(n):
        print(n, "Valid")
    else:
        print(n, "Invalid")

#QUESTION_5
pattern = re.compile(r'^[A-Z][a-zA-Z]* Nakamoto$')

names = ["Satoshi Nakamoto", "Alice Nakamoto", "satoshi Nakamoto"]

for name in names:
    if pattern.match(name):
        print(name, "Match")
    else:
        print(name, "No Match")

#QUESTION_6
pattern = re.compile(
    r'^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$',
    re.IGNORECASE
)

sentences = [
    "Alice eats apples.",
    "BOB EATS CATS.",
    "Carol eats 7 cats."
]

for s in sentences:
    if pattern.match(s):
        print(s, "Match")
    else:
        print(s, "No Match")
'''
#QUESTION_7
def strong(p):
    if len(p) < 8:
        return False
    if not re.search("[A-Z]", p):
        return False
    if not re.search("[a-z]", p):
        return False
    if not re.search("[0-9]", p):
        return False
    return True

pwds = ["Hello123", "hello123", "Hello"]

for p in pwds:
    print(p, "Strong" if strong(p) else "Weak")

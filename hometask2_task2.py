string = raw_input("enter the word:" )
def validate (string):
    return "YES" if string == " ".join(string.split()[::-1]) else "NO"
print validate(string)

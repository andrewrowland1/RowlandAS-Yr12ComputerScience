#program that takes a string and reverses it eg 'hello' goes to 'olleh'
text = input(str("Please input a string"))
print(text)
def reverse(text):
    str = ""
    for reversetext in text:
        str = reversetext + str
    return str
print(reverse(text))

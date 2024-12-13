name = "Dolgova Polina"
letter = ["D", "o", "l", "g", "o", "v", "a", "P", "o", "l", "i", "n", "a"]
letter_str = "_".join(letter)
print(letter_str)

s = letter_str 
su = s.upper()
print(su)
text_1 = su
ASCII_upper = [ord(symbol) for symbol in text_1]
sl = s.lower()
print(sl)
text_2 = sl 
ASCII_lower = [ord(symbol) for symbol in text_2]
print(ASCII_lower)
print("max: ", max(max(ASCII_upper), max(ASCII_lower)))
print("min: ", min(min(ASCII_upper), min(ASCII_lower)))
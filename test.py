text = "This is a sentence."
n = len(text)
if n < 20:
    label = "short"
elif n < 80:
    label = "medium"
else:
    label = "long"
print(label)
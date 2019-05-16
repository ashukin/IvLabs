text = "X-DSPAM-Confidence:    0.8475";
f = text.find(':')
num = text[f+1:]
print(float(num))
import easyocr

image_url = 'https://res.cloudinary.com/ddvajyjou/image/upload/v1706960876/rzse0mcqxbgs8z2pf6lr.png'

reader = easyocr.Reader(['en'])
result = reader.readtext(image_url)
text_ = ""

for (bbox, text, prob) in result:
    text_ += text

print(text_)

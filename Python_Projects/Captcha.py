from captcha.image import ImageCaptcha

k=ImageCaptcha()

image=k.generate("22202")
k.write("22202","Captcha_sample.png")
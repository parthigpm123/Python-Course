from textblob import TextBlob

text = "you are txtx wit misspelled wordss  mey killl"
corrected_words = [str(TextBlob(word).correct()) for word in text.split()]
corrected_text = " ".join(corrected_words)

print(corrected_text)


      
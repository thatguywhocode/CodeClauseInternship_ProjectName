import pyshorteners

original_url=input("Enter url:")

tiny=pyshorteners.Shortener()
shortened_url=tiny.tinyurl.short(original_url)
print("Shortened url:"+ shortened_url)
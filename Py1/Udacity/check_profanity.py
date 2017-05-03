import urllib.request
def read_text():
    quotes = open(r"C:\Users\Saurabh\Desktop\Python\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    contents_of_file = "dentist"
    check_profanity(contents_of_file)
def check_profanity(text_to_check):
    with urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check) as url:
        output = url.read()
    print(output)
    url.close()
read_text()

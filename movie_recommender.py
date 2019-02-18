from bs4 import BeautifulSoup as Soup
import re
import requests as Http

def main(emotion):

    #IMDb URL for Drama genre of
    #movie against emotion Sad
    if ( emotion == "Sad" ):
        url = "http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc"

    #IMDb URL for Musical genre of
    #movie against emotion Disgust
    elif ( emotion == "Disgust" ):
        url = "http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc"

    #IMDb URL for Family genre of
    #movie against emotion Anger
    elif ( emotion == "Anger" ):
        url = "http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc"

    #IMDb URL for Triller genre of
    #movie against emotion Anticipation
    elif ( emotion == "Anticipation" ):
        url = "http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc"

    #IMDb URL for Sport genre of
    #movie against emotion Fear
    elif ( emotion == "Fear" ):
        url = "http://www.imdb.com/search/title?genres=sports&title_type=feature&sort=moviemeter, asc"

    #IMDb URL for Thriller genre of
    #movie for emotion Enjoyment
    elif ( emotion == "Enjoyment" ):
        url = "http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc"

    #IMDb URL for Western genre of
    #movie against emotion Trust
    elif ( emotion == "Trust" ):
        url = "http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc"

    #IMDb URL for Film_noir genre of
    #movie against emotion Surprise
    elif ( emotion == "Surprise" ):
        url = "http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc"

    else :
        print("Invalid emotion")
        exit(1)

    response = Http.get(url)
    data = response.text

    content = Soup(data, "lxml")
    title = content.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    return title

if __name__ == "__main__":
    emotion = input("Enter an Emotion: ")
    page_content = main(emotion)
    count = 0

    if (emotion == "Disgust" or emotion == "Anger" or emotion == "Surprise"):
        for line in page_content:
            temp = str(line).split('>;')
            if (len(temp) == 3):
                print(temp[1][:-3])
            if (count > 13):
                break
            count += 1
    else:
        for line in page_content:
            temp = str(line).split('>')
            if(len(temp) == 3):
                print(temp[1][:-3])
            if (count > 11):
                break
            count += 1
from bs4 import BeautifulSoup
import requests
from skimage import io
import cv2


def process(query):
    url = "https://www.google.co.in/search?q=" + query + "&hl=en&authuser=0&tbm=isch&sxsrf=AOaemvKYGdJleD67B7NyGCzhh36_uKiIuA%3A1635933488488&source=hp&biw=1535&bih=762&ei=MF2CYbTaGK3W1sQPoKGoqAY&iflsig=ALs-wAMAAAAAYYJrQNLL_ELYX-8sSqH0xmHAl1s4ewRH&oq=lol&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQM6CggjEO8DEOoCECc6BwgjEO8DECc6CwgAEIAEELEDEIMBOggIABCxAxCDAVDURli-SWD0V2gBcAB4AIABYYgBmgKSAQEzmAEAoAEBqgELZ3dzLXdpei1pbWewAQo&sclient=img&ved=0ahUKEwi0ss-T9_vzAhUtq5UCHaAQCmUQ4dUDCAY&uact=5"
    width, height = 1280, 720
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    images = soup.find_all('img')
    num = 1
    for image in images[1:]:
        # Starts with 1 because first it recieves Google logo which is locally available in cache
        data_link = image['src']
        name = "file" + str(num)
        num = num + 1
        r = io.imread(data_link)
        cv2.imwrite(name + ".jpg", cv2.resize(r, (width, height)))
        print(name, data_link)

query = input("enter text search query: ")
process(query)
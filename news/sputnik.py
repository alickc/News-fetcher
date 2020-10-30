from constants import *
import constants

def getNews(link, history):
    def getDriver():
        options = Options()
        options.headless = False
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(options=options,
                                  executable_path=constants.driverPath)
        driver.get(link)
        while True:
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[0])
                break
        return driver

    def getParagraphs():
        paragraph = driver.find_elements_by_class_name("b-plainlist__title")
        if len(paragraph) == 0:
            print("NOT A NEWS PAGE")
        return paragraph

    driver = getDriver()
    paragraph = getParagraphs()
    links = []
    for p in paragraph:
        print(p.find_element_by_css_selector('a').get_attribute('href'))
        links.append(p.find_element_by_css_selector('a').get_attribute('href'))
    for link in links:
        if link not in history:
            c= len(os.listdir(constants.path+"sputnik"))
            getContent(link,c)
        else:
            print(link + " is fetched before")


def saveTableTxt():

    files = os.listdir(constants.path + "sputnik")
    links = []
    titles = []
    for file in files:
        with open(constants.path + "sputnik/" + file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            titles.append(lines[1][:-2])
            links.append(lines[0][5:-1])
    writer = "PATH\tTITLE\tLINK\n"
    for i in range(len(files)):
        writer += files[i] + "\t" + titles[i] + "\t" + links[i] + "\n"
    with open(constants.path + "sputnikTable.txt", "a+",
              encoding="utf-8") as f:
        f.write(writer)

def getContent(link,c):

    def getDriver():
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(options=options,
                                  executable_path=constants.driverPath)
        driver.get(link)
        return driver
    def disposer():
        driver.quit()

    def getHeader():
        return driver.find_elements_by_class_name("b-article__header-title")[0].text


    def getParagraphs():
        paragraph = driver.find_elements_by_css_selector("p")
        if len(paragraph) == 0:
            print("NOT A NEWS PAGE")
        return paragraph

    def getTime():
        date = driver.find_elements_by_class_name("b-article__refs-date")[0].text

        return date

    try:
        driver = getDriver()
        header = getHeader()
        paragraph = getParagraphs()
        date = getTime()
        sParagraph: str = ""
        for item in paragraph[3:]:
            # print(item.text)
            if item.text != "" and item.text != "Already have an account? Log in here" and item.text != "There are no Independent Premium comments yet - be the first to add your thoughts":
                sParagraph += (item.text)
        disposer()
        # print(date)
        # print(header)
        # print(sParagraph)
        save(header, sParagraph, date, c, link)
    except Exception as e:
        print(e)


def save(header, paragraph, date, c, link):
    writer = "LINK:" + link + "\nTITLE: " + header + "\n" + paragraph
    if len(paragraph) > 10:
        with open(constants.path + "sputnik/[" + str(c) + "]"+ date.replace(":","-") +".txt", "a+", encoding="utf-8") as f:
            f.write(writer)
            print("saved: " + constants.path + "sputnik/[" + str(c) + "]"+ date.replace(":","-") +".txt")

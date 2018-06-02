from selenium import webdriver
import time
import requests
import json
import re
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
global list_data = list()
FIRST_API ="https://graph.facebook.com/484451281604769/feed?access_token=EAAAAUaZA8jlABAIa3JcJBpOS7hMHVI6TNaHvn0wDkrHzljfywKnqTjBDq0LrYqLYuTEJr9ZBrZC6lbQiYUVPGygf9RqqUg8N4my6FwoIx4lSFSQyx2ILyQ4VQVltLeKnW1GW8jYTUCWSP1PTbZAWnljZBUSvxrVNnU1uvXfFTiwZDZD";


def getContentConfession(link_post):
    driver = webdriver.PhantomJS('./phantomjs');
    driver.get("https://www.facebook.com/");
    time.sleep(10);
    # print (driver.page_source);
    email_input    = driver.find_element_by_id("m_login_email");
    password_input =  driver.find_element_by_id("m_login_password");

    email_input.send_keys("thinhphoho01@gmail.com");
    password_input.send_keys("thinhbka0110");

    driver.find_element_by_name("login").click();

    time.sleep(10);

    driver.get(link_post);
    time.sleep(10);
    html = driver.find_element_by_xpath("//*[@id='pagelet_timeline_main_column']/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/p");
    result = html.html;
    driver.quit();
    return result;

def filterConfession(element):
    # filter by Text
    if bool(re.match('#[0-9]+',element.message):
        if (int(element.likes)* int(element.shares) > 20000):
            return True,element.actions[0].link;
    else:
        return False,"";
    # filter by Like, Share
def filterCommentConfession(element):
    comments = element.comments;
    element.sort(key=extract_time, reverse=True)
    return element[:10];

def extract_time(comments):
    try:
        return int(comments['data']['likes'])
    except:
        return 0

def renderPDF(name):
    doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
def list_data_confession(api):
    headers = {'Content-Type': 'application/json'};
    data = requests.get(api, headers=headers);

    res_data = data.json();

    list_data.extend(res_data);

    if (res["paging"]["next"]):
        list_data_confession(res["paging"]["next"]);
    else:
        return list_data; 

def main():
    all_data = list_data_confession(FIRST_API); 
    name_file ="first_confession";
    for i in range(length(all_data))):
        check, link = filterConfession(all_data[i]);
        if (check):
            text = getContentConfession(link);
            top_comment = filterCommentConfession(all_data[i]);
            count = count +1;
            if (count == 50):
                name_file = "first_confession"+int(count/50);


    # print(res["data"]);
if __name__ == '__main__':
    main()
    
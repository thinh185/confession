from selenium import webdriver
import time
import requests
import json


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



# print (driver.title);
# headers = {'Content-Type': 'application/json'};
# data = requests.get("https://graph.facebook.com/484451281604769/feed?access_token=EAAAAUaZA8jlABAIa3JcJBpOS7hMHVI6TNaHvn0wDkrHzljfywKnqTjBDq0LrYqLYuTEJr9ZBrZC6lbQiYUVPGygf9RqqUg8N4my6FwoIx4lSFSQyx2ILyQ4VQVltLeKnW1GW8jYTUCWSP1PTbZAWnljZBUSvxrVNnU1uvXfFTiwZDZD",
#                      headers=headers);

# res = data.json();
# print(res["data"]);
driver.get("https://www.facebook.com/484451281604769/posts/1726270674089484");
time.sleep(10);
html = driver.find_element_by_xpath("//*[@id='pagelet_timeline_main_column']/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/p");
print (html.get_attribute('innerHTML'));

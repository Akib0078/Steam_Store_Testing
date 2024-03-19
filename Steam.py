from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()


   # 1. Navigating to Steam Store Homepage

driver.get("https://store.steampowered.com/")



try:
    # 2. Searching Dota 2 in the search box
     
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#store_nav_search_term"))
    )

    search_box.send_keys("Dota 2")
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)



    # 3. Saving infos of first and second result


    # Get the details of the first search result
    first_result_name = driver.find_element(By.CSS_SELECTOR, "body.v6.search_page.responsive_page:nth-child(2) div.responsive_page_frame.with_header div.responsive_page_content:nth-child(7) div.responsive_page_template_content:nth-child(6) div.page_content_ctn:nth-child(1) div.page_content div.leftcol.large div.search_results:nth-child(4) div:nth-child(3) a.search_result_row.ds_collapse_flag.app_impression_tracked:nth-child(1) div.responsive_search_name_combined:nth-child(2) div.col.search_name.ellipsis:nth-child(1) > span.title:nth-child(1)").text
    first_result_platforms = driver.find_element(By.CSS_SELECTOR, "body.v6.search_page.responsive_page:nth-child(2) div.responsive_page_frame.with_header div.responsive_page_content:nth-child(7) div.responsive_page_template_content:nth-child(6) div.page_content_ctn:nth-child(1) div.page_content div.leftcol.large div.search_results:nth-child(4) a.search_result_row.ds_collapse_flag.app_impression_tracked:nth-child(1) div.responsive_search_name_combined:nth-child(2) div.col.search_name.ellipsis:nth-child(1) div:nth-child(2) > span.platform_img.win:nth-child(1)").get_attribute("alt")
    first_result_release_date = driver.find_element(By.XPATH, "//div[contains(text(),'9 Jul, 2013')]").text
    first_result_review_summary = driver.find_element(By.CSS_SELECTOR, "body.v6.search_page.responsive_page:nth-child(2) div.responsive_page_frame.with_header div.responsive_page_content:nth-child(7) div.responsive_page_template_content:nth-child(6) div.page_content_ctn:nth-child(1) div.page_content div.leftcol.large div.search_results:nth-child(4) div:nth-child(3) a.search_result_row.ds_collapse_flag.app_impression_tracked:nth-child(1) div.responsive_search_name_combined:nth-child(2) div.col.search_reviewscore.responsive_secondrow:nth-child(3) > span.search_review_summary.positive").get_attribute("data-tooltip-html")
    first_result_price = driver.find_element(By.XPATH, "//body/div[1]/div[7]/div[6]/form[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/a[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]").text

    time.sleep(5)

    print("First Result:")
    print("Name:", first_result_name)
    print("Platforms:", first_result_platforms)
    print("Release Date:", first_result_release_date)
    print("Review Summary:", first_result_review_summary)
    print("Price:", first_result_price)
    print()



    # Get the details of the second search result
    second_result_name = driver.find_element(By.XPATH, "//span[contains(text(),'Dota 2 Player Profiles')]").text
    second_result_platforms = driver.find_element(By.CSS_SELECTOR, "body.v6.search_page.responsive_page:nth-child(2) div.responsive_page_frame.with_header div.responsive_page_content:nth-child(7) div.responsive_page_template_content:nth-child(6) div.page_content_ctn:nth-child(1) div.page_content div.leftcol.large div.search_results:nth-child(4) a.search_result_row.ds_collapse_flag.app_impression_tracked:nth-child(2) div.responsive_search_name_combined:nth-child(2) div.col.search_name.ellipsis:nth-child(1) div:nth-child(2) > span.platform_img.streamingvideoseries").get_attribute("alt")
    second_result_release_date = driver.find_element(By.XPATH, "//div[contains(text(),'13 Nov, 2015')]").text
    second_result_review_summary = driver.find_element(By.CSS_SELECTOR, "body.v6.search_page.responsive_page:nth-child(2) div.responsive_page_frame.with_header div.responsive_page_content:nth-child(7) div.responsive_page_template_content:nth-child(6) div.page_content_ctn:nth-child(1) div.page_content div.leftcol.large div.search_results:nth-child(4) div:nth-child(3) a.search_result_row.ds_collapse_flag.app_impression_tracked:nth-child(2) div.responsive_search_name_combined:nth-child(2) div.col.search_reviewscore.responsive_secondrow:nth-child(3) > span.search_review_summary.positive").get_attribute("data-tooltip-html")
    second_result_price = driver.find_element(By.XPATH, "//body/div[1]/div[7]/div[6]/form[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/a[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]").text

    time.sleep(5)

    print("second Result:")
    print("Name:", second_result_name)
    print("Platforms:", second_result_platforms)
    print("Release Date:", second_result_release_date)
    print("Review Summary:", second_result_review_summary)
    print("Price:", second_result_price)
    print()



    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#store_nav_search_term"))
    )

    search_box.send_keys(second_result_name)
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)

finally:
    # Closing the browser
    driver.quit()




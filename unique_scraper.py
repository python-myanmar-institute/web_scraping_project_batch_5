import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
from datetime import datetime

def create_bsObj(website_url):
    """Create a beautifulsoup object for the input URL."""
    # Request data from the website
    response = requests.get(website_url)
    status_code = response.status_code # status code attribute
    if status_code == 200:
        # Extract web code
        web_data = response.text
        # Create a beautifulsoup object from web data
        bsObj = BeautifulSoup(web_data, "html.parser")
    
    return bsObj

def create_page_url_list(website_url):
    """Create web page urls list."""
    # Request data from the website
    main_bsObj = create_bsObj(website_url)
    # Extract Web Page count
    page_count_tag = main_bsObj.find("span", class_="pagination__page-count")
    page_count = page_count_tag.text
    page_count = int(page_count[-1])
    #print(page_count)

    # Create web page urls for each page
    page_url_list = []
    for page_num in range(1, page_count+1):
        page_url = website_url + "?page=" + str(page_num)
        page_url_list.append(page_url)
        
    return page_url_list

def extract_name(item_tag_var):
    """Extract product name from item tag"""
    item_name_tag = item_tag_var.find("a", class_="product-item__title text--strong link")
    item_name = item_name_tag.text
    return item_name

def extract_price(item_tag_var):
    """Extract product name from item tag"""
    item_price_tag = item_tag_var.find("span", class_="price")
    item_price = item_price_tag.text
    item_price = item_price.replace(",", "")
    item_price = item_price.replace("K", "")
    item_price = float(item_price)
    return item_price

def extract_stock(item_tag_var):
    """Extract product stock/inventory from item tag"""
    stock_class_list = ["product-item__inventory inventory inventory--low",
                    "product-item__inventory inventory inventory--high",
                    "product-item__inventory inventory"]
    for stock_class in stock_class_list:
        item_stock_tag = item_tag_var.find("span", class_=stock_class)
        if item_stock_tag != None: # we found the data
            break
    
    item_stock = item_stock_tag.text
    return item_stock

def extract_link(item_tag_var):
    """Extract Product Link from item tag"""
    item_link_tag = item_tag_var.find("a", class_="product-item__title text--strong link")
    item_link = item_link_tag.get("href")
    main_website = "https://unique.com.mm"
    item_link = main_website + item_link
    return item_link

def export_as_excel(name_list, price_list, stock_list, link_list):
    """Export data as Excel file"""
    df = pd.DataFrame({"Name":name_list,
                       "Price":price_list,
                       "Stock":stock_list,
                       "Link":link_list})
    
    current_dt = datetime.now()
    current_dt_format = current_dt.strftime("%Y-%m-%d %H-%M-%S")
    # Insert datetime column
    df["Extracted DateTime"] = current_dt
    
    # Export as excel
    df.to_excel(f"C:\\Users\\M\\Desktop\\Python Scripts - Batch 5\\Exported Data Collection\\Exported Data {current_dt_format}.xlsx", index=False)
    df.to_excel("Last Update Data.xlsx", index=False)
    print("Product info are exported as excel file successfully...")
    return None


################################# Main ################################################################################
def main():
    # Setup main url
    my_url = "https://unique.com.mm/collections/mobile-phone"

    # Create a list for web page url
    my_page_url_list = create_page_url_list(my_url)

    # Data Extraction from each page url
    item_name_list =[]
    item_price_list = []
    item_stock_list = []
    item_link_list = []
    for page_url in tqdm(my_page_url_list):
        # Create bs4 object for web page
        page_bsObj = create_bsObj(page_url)
        # Use find all method to search data tags
        item_tags_list = page_bsObj.find_all("div", "product-item__info-inner")
        
        for item_tag in item_tags_list:
            
            # Extract Name
            item_name = extract_name(item_tag)
            item_name_list.append(item_name)
            
            # Extract Price
            item_price = extract_price(item_tag)
            item_price_list.append(item_price)
            
            # Extract Stock
            try:
                item_stock = extract_stock(item_tag)
                item_stock_list.append(item_stock)
            except:
                print("There was an error in stock.")
                raise
            
            # Extract Link
            item_link = extract_link(item_tag)
            item_link_list.append(item_link)
    print(len(item_name_list))
    print(len(item_price_list))
    print(len(item_stock_list))
    print(len(item_link_list))
    
    # Export as excel
    export_as_excel(name_list=item_name_list,
                    price_list=item_price_list,
                    stock_list=item_stock_list,
                    link_list=item_link_list)

if __name__ == "__main__":
    main()
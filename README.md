# Web Scraping Project Batch 5
# 📱 Unique.com.mm Mobile Phone Web Scraper

A Python-based web scraper that collects **mobile phone product information** from [Unique.com.mm](https://unique.com.mm/) and exports the results into an Excel spreadsheet.

The scraper automatically navigates through all available pages in the mobile phone collection and extracts product details such as **name, price, stock status, and product URL**.

---

## 🚀 Features

* Scrapes mobile phone products from Unique.com.mm
* Automatically detects the number of pagination pages
* Extracts:

  * 📱 Product Name
  * 💰 Product Price
  * 📦 Stock / Inventory Status
  * 🔗 Product Link
* Displays scraping progress using `tqdm`
* Adds an extraction timestamp to the dataset
* Exports the collected data to Excel
* Creates both:

  * A timestamped historical Excel file
  * A `Last Update Data.xlsx` file containing the latest results

---

## 🛠️ Technologies Used

| Technology    | Purpose                              |
| ------------- | ------------------------------------ |
| Python        | Main programming language            |
| Requests      | Sending HTTP requests to the website |
| BeautifulSoup | Parsing and extracting HTML data     |
| Pandas        | Creating and managing the dataset    |
| tqdm          | Displaying scraping progress         |
| openpyxl      | Writing data to Excel                |
| datetime      | Recording extraction date and time   |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/unique-mobile-phone-scraper.git
cd unique-mobile-phone-scraper
```

### 2. Install the required packages

```bash
pip install requests beautifulsoup4 tqdm pandas openpyxl
```

Or create a `requirements.txt` file:

```txt
requests
beautifulsoup4
tqdm
pandas
openpyxl
```

Then install everything with:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Python script:

```bash
python scraper.py
```

The scraper starts from the mobile phone collection page:

```text
https://unique.com.mm/collections/mobile-phone
```

It first determines how many pages are available and then visits each page to collect product information.

---

## 🔄 How It Works

The scraping process follows these steps:

```text
Unique.com.mm Mobile Phone Collection
                │
                ▼
       Detect Page Count
                │
                ▼
       Generate Page URLs
                │
                ▼
       Visit Each Web Page
                │
                ▼
       Find Product Elements
                │
                ▼
       Extract Product Data
        ┌───────┼────────┐
        ▼       ▼        ▼
      Name    Price    Stock
                │
                ▼
             Link
                │
                ▼
       Create Pandas DataFrame
                │
                ▼
          Export to Excel
```

---

## 📊 Data Collected

The resulting Excel file contains the following columns:

| Column               | Description                               |
| -------------------- | ----------------------------------------- |
| `Name`               | Product name                              |
| `Price`              | Product price                             |
| `Stock`              | Current inventory/stock status            |
| `Link`               | Product URL                               |
| `Extracted DateTime` | Date and time when the data was collected |

### Example

| Name              |     Price | Stock     | Link        | Extracted DateTime  |
| ----------------- | --------: | --------- | ----------- | ------------------- |
| Example Phone     | 1,299,000 | In stock  | Product URL | 2026-09-03 22:00:00 |
| Example Phone Pro | 1,599,000 | Low stock | Product URL | 2026-09-03 22:00:00 |

---

## 📁 Output Files

The script creates two Excel files.

### Timestamped file

A historical copy is created using the extraction date and time:

```text
Exported Data 2026-09-03 22-00-00.xlsx
```

This allows previous scraping results to be preserved.

### Latest data

The most recent results are also saved as:

```text
Last Update Data.xlsx
```

This file is overwritten each time the scraper runs.

---

## 🧩 Main Functions

### `create_bsObj()`

Sends an HTTP request to a URL and creates a BeautifulSoup object for parsing the HTML.

```python
def create_bsObj(website_url):
```

---

### `create_page_url_list()`

Determines the number of pages in the collection and generates the URL for each page.

```python
def create_page_url_list(website_url):
```

For example:

```text
?page=1
?page=2
?page=3
...
```

---

### `extract_name()`

Extracts the product name from the product HTML element.

```python
def extract_name(item_tag_var):
```

---

### `extract_price()`

Extracts and converts the product price into a numeric value.

```python
def extract_price(item_tag_var):
```

The function also removes commas and the `K` character before converting the value to `float`.

---

### `extract_stock()`

Extracts the current stock/inventory information.

```python
def extract_stock(item_tag_var):
```

The scraper checks several possible CSS classes because the website may use different classes depending on the inventory status.

---

### `extract_link()`

Extracts the product URL and converts the relative URL into a complete URL.

```python
def extract_link(item_tag_var):
```

---

### `export_as_excel()`

Creates a Pandas DataFrame and exports the scraped data to Excel.

```python
def export_as_excel(name_list, price_list, stock_list, link_list):
```

An extraction timestamp is also added to the dataset.

---

## ⚙️ Configuration

The target website can be changed inside the `main()` function:

```python
my_url = "https://unique.com.mm/collections/mobile-phone"
```

For example, if another product collection on the website follows the same HTML structure, you can replace the URL with the appropriate collection URL.

> **Note:** The scraper depends on the website's current HTML structure. If Unique.com.mm changes its page layout, CSS classes, or pagination system, the extraction functions may need to be updated.

---

## ⚠️ Important Considerations

### Website Changes

This scraper relies on specific HTML classes such as:

```text
product-item__info-inner
product-item__title
product-item__inventory
price
```

Changes to the website's HTML structure may cause the scraper to stop working correctly.

### Request Rate

The script sends HTTP requests to multiple pages. Consider adding a delay between requests if necessary:

```python
import time

time.sleep(1)
```

This can help reduce the load placed on the target website.

### Terms of Service

Before scraping a website, make sure your use complies with the website's **Terms of Service**, `robots.txt`, and applicable laws or policies. Use responsible request rates and avoid collecting data that you are not authorized to collect.

---

## 🔮 Possible Improvements

Some useful improvements for future versions include:

* [ ] Add request timeout handling
* [ ] Add retry logic for failed requests
* [ ] Add logging instead of `print()`
* [ ] Add configurable output directories
* [ ] Move the target URL into a configuration file
* [ ] Add command-line arguments
* [ ] Add request delays
* [ ] Handle missing product information gracefully
* [ ] Detect pagination more robustly
* [ ] Export to CSV in addition to Excel
* [ ] Compare current data with previous scraping results
* [ ] Detect price changes
* [ ] Detect stock-status changes
* [ ] Schedule automatic scraping

---

## 📂 Suggested Project Structure

```text
unique-mobile-phone-scraper/
│
├── scraper.py
├── requirements.txt
├── README.md
│
└── output/
    ├── Last Update Data.xlsx
    └── Exported Data YYYY-MM-DD HH-MM-SS.xlsx
```

---

## 👨‍💻 Author

**Your Name**

If you found this project useful, feel free to ⭐ star the repository and explore the code.

---

## 📄 License

This project is intended for educational and personal data-collection purposes.

Add an appropriate license to the repository if you plan to distribute or reuse the project publicly.


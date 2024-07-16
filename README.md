# Church Scraper

This Scrapy project scrapes data for 351,000 churches from [churchangel.com](https://www.churchangel.com/) at a rate of approximately 250 items per minute.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/church_scraper.git
    cd church_scraper
    ```

2. Install the required packages:
    ```sh
    pip install scrapy
    ```

## Usage

Run the spider:
```sh
scrapy crawl Church -O response.json
```

## Scraped Data
The spider collects the following information for each church:

- Title
- Category
- Telephone
- Description
- Website
- Link to the church's page
- Link to the church's category page

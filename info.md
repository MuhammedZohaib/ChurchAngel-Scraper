# Chruch Angels

churches = response.css("div.sabai-col-xs-9.sabai-directory-main").getall()
title = response.css("div.sabai-directory-title a::text").get()
church_link = response.css("div.sabai-directory-title a::attr('href')").get()
church_category = response.css("div.sabai-directory-category a::text").get()
church_category_link = response.css("div.sabai-directory-category a::attr('href')").get()
church_tel = response.css("div.sabai-directory-contact-tel span.sabai-hidden-xs::text").get()
church_website = response.css("div.sabai-directory-contact-website a::attr('href')").get()
church_description = response.css("div.sabai-directory-body::text").get().strip()
next_page_url = response.css('div.sabai-pull-right > div > a:last-child::attr("href")').get()

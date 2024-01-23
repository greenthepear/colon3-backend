from . import _shared as p
import re

def scrape_ciapkowo_pl() -> list:
    soup = p.get_page_contents("https://ciapkowo.pl/filter/koty/")

    pages_number = int(soup.find_all('li', class_='page-item')[-2].text.strip())
    #print(pages_number)
    catboxes = soup.find_all('div', class_="card h-100")
    #print(catboxes)

    allcats = []
    for page_num in range(pages_number):
        if pages_number != 0:
            soup = p.get_page_contents(f"https://ciapkowo.pl/filter/koty/page/{page_num+1}/")
            catboxes = soup.find_all('div', class_="card h-100")
        #print(f"\nOn page {page_num+1} found {len(catboxes)} cat boxes.")
        for i, box in enumerate(catboxes):
            name = box.find('h5', class_="card-title text-center").text.strip()

            info_divs = box.find_all('div', class_="value text-right")
            sex_text = info_divs[0].text.strip()
            sex = "F" if sex_text == "Kotka" else "M"

            age_text = info_divs[1].text.strip()

            age_find = re.findall(r'\d+', age_text)
            age = 0
            if len(age_find) != 0:
                age = age_find[0]


            url = box.find('a', class_="btn btn-primary stretched-link").get('href')
            imglink = box.find('img', class_= "card-img-top wp-post-image").get('src')

            #print(f"{name}: {sex}, {age}\n{url}\n{imglink}")

            allcats.append({"listing_url":url,
                            "cat_name":name,
                            "cat_sex":sex,
                            "source":"ciapkowo.pl",
                            "image_url":imglink,
                            "cat_age":age,
                            })
    
    return allcats



if __name__ == "__main__":
    scrape_ciapkowo_pl()
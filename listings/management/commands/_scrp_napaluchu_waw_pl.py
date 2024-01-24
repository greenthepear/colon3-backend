from . import _shared as p
import re

def scrape_napaluchu_waw_pl() -> list:
    soup = p.get_page_contents("https://napaluchu.waw.pl/zwierzeta/zwierzeta-do-adopcji/?pet_species=2")

    pages_number = len(soup.find_all('div', class_='row clearfix text-center')[-1].find_all('a'))

    catboxes = soup.find_all('div', class_="pet-block col-md-4 col-sm-12 col-xs-12")

    allcats = []
    for page_num in range(pages_number):
        if pages_number != 0:
            soup = p.get_page_contents(f"https://napaluchu.waw.pl/zwierzeta/zwierzeta-do-adopcji/?pet_page={page_num+1}&pet_species=2")
            catboxes = soup.find_all('div', class_="pet-block col-md-4 col-sm-12 col-xs-12")
        #print(f"\nOn page {page_num+1} found {len(catboxes)} cat boxes.")
        for i, box in enumerate(catboxes):
            namea = box.find('h3', class_="pets-list-pet-name").find('a')
            url = "https://napaluchu.waw.pl" + namea.get('href')
            name = namea.text.strip().split()[0]
            
            if re.match(r'\d\d\d\d\/\d\d',name) != None:
                name = "?"

            info = box.find('li', class_="pet-tags").text.split(", ")
            if len(info) < 2:
                print("Bad splitting of pet tag: ", box.find('li', class_="pet-tags").text)
                return

            sex = 'M' if info[0] == "samiec" else 'F'
            if 'mies' in info[1]:
                age = 0
            else:
                age = int(re.findall(r'\d+', info[1])[0])

            imglink = box.find('img', class_="pets-list-pet-image").get('src')

            #print(f"{name}: {sex}, {age}\n{url} - {imglink}")

            allcats.append({"listing_url":url,
                            "cat_name":name,
                            "cat_sex":sex,
                            "source":"napaluchu.waw.pl",
                            "image_url":imglink,
                            "cat_age":age,
                            })
    
    return allcats

if __name__ == "__main__":
    scrape_napaluchu_waw_pl()
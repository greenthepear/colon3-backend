from . import _shared as p

def scrape_schronisko_lodz_pl() -> list:
    soup = p.get_page_contents('https://schronisko-lodz.pl/?p=adopcje&a=search&type=kot')
    pages_number_raw = soup.find('div', style='width: 100%; border-style: solid; border-width: 0px; clear: both;').text

    #print(pages_number_raw)
    pages_nums = pages_number_raw.split(" ")
    #print(pages_nums)
    number_of_pages = len(pages_nums) - 1
    #print(number_of_pages)

    catboxes = soup.find_all('div', class_ = 'animal_box')

    allcats = []

    for page_num in range(number_of_pages):
        if page_num != 0:
            soup = p.get_page_contents(f"https://schronisko-lodz.pl/?p=adopcje&a=search&type=kot&page={page_num+1}")
            catboxes = soup.find_all('div', class_ = 'animal_box')
        for i, box in enumerate(catboxes):
            name = box.find("span", style="font-size: 18px; font-weight: bold;").text
            info = box.find("span", id="animal_box_small").text
            infosplit = info.split()

            img = box.find("img")
            imglink = "https://schronisko-lodz.pl/" + img["src"]

            sex = "F" if infosplit[0] == "kotka" else "M"

            age = int(infosplit[1].strip("()"))

            raw_link = box.find("a", class_="animal_box_link").get('href')
            listing_link = f"https://schronisko-lodz.pl/{raw_link.replace('&amp','')}"

            #print(f"\n\t{page_num+1}.{i+1}:\nName: {name}\nSex: {sex}\nAge: {age}\nLink: {listing_link}")


            allcats.append({"listing_url":listing_link,
                            "cat_name":name,
                            "cat_sex":sex,
                            "source":"schronisko-lodz.pl",
                            "image_url":imglink,
                            "cat_age":age,
                            })

    #print(f"Cats found: {len(allcats)}")
    #print(allcats)
    return allcats

if __name__ == "__main__":
    scrape_schronisko_lodz_pl()
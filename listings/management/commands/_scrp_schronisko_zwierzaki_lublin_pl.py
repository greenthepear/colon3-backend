from . import _shared as p
import re

def scrape_schronisko_zwierzaki_lublin_pl() -> list:
    soup = p.get_page_contents("http://schronisko-zwierzaki.lublin.pl/index.php?option=com_djcatalog&view=show&cid=2&Itemid=17")

    pages_number = int(soup.find(
        'td', class_="djcat_pag").findChildren(
            recursive=False)[-3].text.strip())
    
    catboxes = soup.find_all('tr', class_="sectiontableentry2")

    catboxes.extend(soup.find_all('tr', class_="sectiontableentry1"))

    allcats = []
    for page_num in range(pages_number):
        if pages_number != 0:
            soup = p.get_page_contents(
                f"http://schronisko-zwierzaki.lublin.pl/index.php?option=com_djcatalog&view=show&cid=2&Itemid=17&limitstart={30*page_num}")
            catboxes = soup.find_all('tr', class_="sectiontableentry2")
            catboxes.extend(soup.find_all('tr', class_="sectiontableentry1"))
        #print(f"\nOn page {page_num+1} found {len(catboxes)} cat boxes.")
        for i, box in enumerate(catboxes):
            title = box.find('td', class_="djcat_product")
            url = "http://schronisko-zwierzaki.lublin.pl" + title.find('a').get('href')
            name = title.text.strip().capitalize()
            name = name.replace('.','').replace(',','')
            name = re.sub(r'[0-9]','', name)

            info = box.find('td', class_="djcat_intro").text
            sex = 'F'
            if "samiec" in info or "męska" in info:
                sex = 'M'
            
            year = re.findall(r'Rok urodzenia: \d\d\d\d', info)[0]
            age = 2024 - int(re.findall(r'\d\d\d\d', year)[0])
            
            imglink = box.find('img').get('src')

            #print(f"{name}: {sex} - {age}\n{url}\n{imglink}")

            allcats.append({"listing_url":url,
                            "cat_name":name,
                            "cat_sex":sex,
                            "source":"schronisko-zwierzaki.lublin.pl",
                            "image_url":imglink,
                            "cat_age":age,
                            })
            
    return allcats



if __name__ == "__main__":
    scrape_schronisko_zwierzaki_lublin_pl()
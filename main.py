import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_max_resolution_image(destination, city):
    query = f"{destination} {city}"
    url = f"https://www.bing.com/images/search?q={query}"

    driver = webdriver.Chrome()
    driver.get(url)

    try:
        image_link = driver.find_element(By.CLASS_NAME, "iusc")
        driver.get(image_link.get_attribute("href"))

        time.sleep(1)

        container = driver.find_element(By.CLASS_NAME, "imgContainer")
        image = container.find_element(By.TAG_NAME, "img")

        current_image_url = image.get_attribute("src")
    except Exception as e:
        current_image_url = None

    driver.quit()

    return current_image_url

# Example usage:
city = "Bali"

destinationDescriptions = ["Ubud: Known for its lush rice terraces, art scene, and cultural heritage.",
"Kuta: Famous for its lively nightlife, surfing beaches, and shopping.",
"Seminyak: A more upscale area with trendy boutiques, beach clubs, and fine dining.",
"Canggu: A relaxed coastal town popular among surfers and digital nomads.",
"Jimbaran: Known for its seafood restaurants and beautiful beaches.",
"Nusa Dua: Home to luxurious resorts and pristine white-sand beaches.",
"Uluwatu: Offers stunning clifftop views, the Uluwatu Temple, and great surfing.",
"Sanur: A laid-back beach town with a great sunrise view and water sports.",
"Amed: A peaceful coastal village known for its snorkeling and diving spots.",
"Lovina: Located in the north, known for dolphin watching and hot springs.",
"Gili Islands: A group of three small islands near Bali, known for their snorkeling and diving spots.",
"Nusa Penida: A rugged island with dramatic landscapes and amazing viewpoints.",
"Tegallalang: Famous for its picturesque rice terraces.",
"Tirta Gangga: Home to a beautiful water palace and lush gardens.",
"Sidemen: A serene village surrounded by rice paddies and great for trekking."]

for destinationDescription in destinationDescriptions:
    destination = destinationDescription.split(":")[0]
    description = destinationDescription.split(": ")[1]
    max_resolution_image_url = get_max_resolution_image(destination, city)
    f = open("itineraries.txt", "a")
    
    if max_resolution_image_url:
        f.write(f"[\n'name' => '{destination}',\n'description' => '{description}',\n'image_url' => '{max_resolution_image_url}',\n'coordinates' => DB::raw(\"POINT(-8.721415, 115.168634)\"),\n'price' => random_int(50000, 500000),\n'destination_id' => Destination::where('name', '{city}')->first()->id,\n'type_id' => DB::table('itinerary_types')->where('name', 'Water Activity')->first()->id\n],\n")
    else:
        print(f"No image found for {destination}\n")

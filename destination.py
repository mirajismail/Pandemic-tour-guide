def destinations(key):

    key = key.strip().upper()
    
    country = {'CANADA':["CN Tower","Parliament Hill","Banff National Park","Niagara Falls"], 
           'INDIA':["Mumbai", "Jaipur", "Taj Mahal", "Ranthambore National Park"],
           'CHINA':["Great Wall", "Forbidden City", "Tiananmen Square", "Temple of Heaven"],
           'USA':["Grand Canyon", "Yosemite National Park", "Lake Tahoe", "Golden Gate Bridge"],
           'RUSSIA':["State Hermitage Museum", "St. Basil's Cathedral", "The Moscow Kremlin", "Red Square"],
           'SPAIN':["La Sagrada Familia", "Park Guell", "Alhambra", "Museo Nacional de Prado"],
           'THAILAND':["The Grand Palace", "Wat Arun Ratchawararam Ratchaworamahawihan","Railay Beach","Chatuchak Weekend Market"],
           'AUSTRALIA':["Great Barrier Reef", "Sydney Opera House", "Uluru", "Kakadu National Park"],
           'EGYPT':["The Egyptian Museum", "Valley of the Kings", "Karmak", "Great Sphinx of Giza"],
           'SOUTH AFRICA':["Kruger National Park", "Maclear's Beacon", "KirstenBosch National Botanical Garden", "Boulder's Beach"],
           'MEXICO':["Chichen Itza", "Tulum Archaeological Zone", "Frida Kahlo Museum", "Xcaret Park"],
           'BRAZIL':["Christ the Redeemer", "Sugarloaf Mountain","Museum of Art of Sao Paulo Assis Chateaubriand", "Copacabana Beach"],
           'SAUDI ARABIA':["Masjid al-Haram", "Abraj Al-Bait Towers", "Center Point", "Masmak Fortress"],
           'ETHIOPIA':["Simien Mountains National Park", "Rock-Hewn Churches, Lalibela", "Blue Nile Falls", "Bale Mountains National Park"],
            'ALGERIA': ["Monument of the Martyr","Basilique Notre Dame d'Afrique", "Fort Santa Cruz"],
            'NIGERIA':["Freedom Park Lagos","Kajuru Castle","Abuja National Mosque", "Gurara Falls"]}
    return country[key]
        

#tester code
if __name__ == "__main__":
    print(destinations("canada"))
    print(destinations("mexICO"))

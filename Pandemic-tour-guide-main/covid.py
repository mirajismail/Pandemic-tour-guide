from covidpy import CountryData

import countryinfo as ci

import pprint


#countries = cp.ListCountries()
#world = cp.WorldData()


'''
returns a dictionary with:

{'country': country['Country_Name'], 'cases': country["Active_Cases"], 'rating': rating}
'''

def getCovidStats(name):

    '''EXAMPLE RESULT IS DICTIONARY
{
    'Country_Name': 'BANGLADESH', 
    'Total_Cases': 777397, 
    'New_Cases': 0, 
    'Total_Deaths': 12045, 
    'New_Deaths': 0, 
    'Total_Recovered': 718249, 
    'New_Recovered': 0, 
    'Active_Cases': 47103, 
    'Serious_Cases': 1120, 
    'Total_Tests': 5677222
}
    '''
    name = name.lower().strip()
    
    country = CountryData(name)
    population = ci.CountryInfo(name).population()


    #method for ranking countries
    percentage = country["Active_Cases"]/(country['Total_Cases'] - country['Total_Recovered'])

    #print(percentage)
                                                 

    #print(percentage)
    
    rating = 0

    if percentage < 1:
        rating = round(10 * (1-percentage), 1)

    #print(rating)

    result = {'country': country['Country_Name'],
              'cases': country["Active_Cases"],
              'rating': rating}

    return result


#tester code
if __name__ == "__main__":

    countryDict = {"Canada" : (255, 0, 0),
               "India" : (255, 138, 0),
               "USA": (52, 100, 235),
               "Mexico": (13, 107, 21),
               "Brazil": (10,209,27),
               "Spain": (235, 231, 30),
               "South Africa": (181,5,38),
               "Ethiopia": (27, 128, 135),
               "Egypt": (225, 227, 209),
               "Saudi Arabia": (3,37,84),
               "Russia": (134, 17,17),
               "Thailand": (88,3,110),
               "China": (189, 30, 57),
               "Australia": (9, 66, 181),
               "Algeria": (60,255,0),
               "Nigeria": (204, 0, 255)}
    
    for key in countryDict.keys():
        pprint.pprint(getCovidStats(key))

    #pprint.pprint(countries)

conversion = {"M": 1000000,
             "B": 1000000000}

names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

dmg = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M',
           '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B',
           '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


def updated_damages(damages):
    new_damages = []
    for item in damages:
        if item == 'Damages not recorded':
            new_damages.append(item)
        else:
            modifier = item[-1]
            value = item[:-1]
            new_modifier = conversion[modifier]
            new_damages.append(float(value) * new_modifier)
    return new_damages


def combine_lists_name(names, months, years, max_sustained_winds, areas_affected, deaths, damages):
    hurricanes = {}
    keys = ["Name", "Month", "Year", "Max Sustained Wind", "Areas Affected", "Deaths", "Damages"]
    newdmg = updated_damages(damages)
    for index in range(0,len(names)):
        values = [names[index], months[index], years[index], max_sustained_winds[index], areas_affected[index], deaths[index], newdmg[index]]
        temp_dict = {key:value for key,value in zip(keys, values)}
        hurricanes[names[index]] = temp_dict

    return hurricanes


def combine_lists_year(names, months, years, max_sustained_winds, areas_affected, deaths, damages):
    hurricanes = {}
    keys = ["Name", "Month", "Year", "Max Sustained Wind", "Areas Affected", "Deaths", "Damages"]
    newdmg = updated_damages(damages)
    for index in range(0,len(years)):
        if years[index] in hurricanes:
            values = [names[index], months[index], years[index], max_sustained_winds[index], areas_affected[index], deaths[index], newdmg[index]]
            temp_dict = {key:value for key, value in zip(keys, values)}
            hurricanes[years[index]] = [hurricanes[years[index]], temp_dict]
        else:
            values = [names[index], months[index], years[index], max_sustained_winds[index], areas_affected[index], deaths[index], newdmg[index]]
            temp_dict = {key:value for key, value in zip(keys, values)}
            hurricanes[years[index]] = temp_dict
    return hurricanes


def area_frequency(areas_affected):
    frequencies = {}
    for item in areas_affected:
        for area in item:
            if area in frequencies:
                frequencies[area] += 1
            else:
                frequencies[area] = 1
    return frequencies


def most_frequent_area(frequencies):
    high_score = 0
    area = ''
    for item in frequencies:
        if frequencies[item] > high_score:
            high_score = frequencies[item]
            area = item
    return [area, high_score]


def most_deaths(hurricanes):
    high_score = 0
    name = ''
    for item in hurricanes:
        if hurricanes[item]["Deaths"] > high_score:
            high_score = hurricanes[item]["Deaths"]
            name = hurricanes[item]["Name"]
    return [name, high_score]


def mortality_scale(hurricanes):
    mortality_rating = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000,
                   5: 1000000000}
    mortalities = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[],}
    for item in hurricanes:
        for counter in mortality_rating:
            if hurricanes[item]["Deaths"] > mortality_rating[counter] and hurricanes[item]["Deaths"] <= mortality_rating[counter+1]:
                mortalities[counter].append(hurricanes[item]["Name"])

    return mortalities


def most_damage(hurricanes):
    high_score = 0
    name = ''
    for item in hurricanes:
        if (hurricanes[item]["Damages"]) == "Damages not recorded":
            pass
        elif hurricanes[item]["Damages"] > high_score:
            high_score = hurricanes[item]["Damages"]
            name = hurricanes[item]["Name"]
    return [name, high_score]

def damage_scale(hurricanes):
    damage_rating = {0: 0,
                     1: 100000000,
                     2: 1000000000,
                     3: 10000000000,
                     4: 50000000000,
                     5: 100000000000000000000}
    total_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [],}
    for item in hurricanes:
        if (hurricanes[item]["Damages"]) == "Damages not recorded":
            pass
        else:
            for counter in damage_rating:
                if hurricanes[item]["Damages"] > damage_rating[counter] and hurricanes[item]["Damages"] <= damage_rating[counter + 1]:
                    total_damage[counter].append(hurricanes[item]["Name"])

    return total_damage


print(damage_scale(combine_lists_name(names, months, years, max_sustained_winds, areas_affected, deaths, damages)))
#print(most_damage(combine_lists_name(names, months, years, max_sustained_winds, areas_affected, deaths, dmg)))
#print(mortality_scale(combine_lists_name(names, months, years, max_sustained_winds, areas_affected, deaths)))
#print(most_deaths(combine_lists_name(names, months, years, max_sustained_winds, areas_affected, deaths)))

#print(most_frequent_area(area_frequency(areas_affected)))
#print(area_frequency(areas_affected))
#print(combine_lists_name(names, months, years, max_sustained_winds, areas_affected, deaths))
#print(updated_damages(dmg))
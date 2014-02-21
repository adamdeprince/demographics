from demographics.data.us.race import data as us_race_data
from demographics.data.us.gender import data as us_gender_data
from collections import namedtuple 

Demographic = namedtuple('Demographic', ('first', 'last', 'popularity', 'male', 'female', 'white', 'black', 'hispanic', 'aian', 'api', 'multi', 'raw'))

USRaw = namedtuple('USRaw', ('gender', 'race'))

def us_demographics(firstname, lastname):
    firstname = firstname.upper()
    lastname = lastname.upper()

    gender_data = us_gender_data[firstname]
    race_data = us_race_data[lastname]
    
    p = (gender_data.m + gender_data.f) * race_data.rate
    
    return Demographic(firstname.lower(), 
                       lastname.lower(),
                       p,
                       gender_data.m / (gender_data.m + gender_data.f),
                       gender_data.f / (gender_data.m + gender_data.f),
                       race_data.white,
                       race_data.black, 
                       race_data.hispanic,
                       race_data.aian,
                       race_data.api,
                       race_data.multi,
                       USRaw(gender_data, race_data))


def us_demographics_as_dict(firstname, lastname):
    d = us_demographics(firstname, lastname)
    return dict(first=d.first,
                last=d.last,
                popularity=d.popularity,
                male=d.male,
                female=d.female,
                white=d.white,
                black=d.black,
                hispanic=d.hispanic,
                aian=d.aian,
                api=d.api,
                multi=d.multi,
                raw=dict(
                    gender=d.raw.gender,
                    raced=d.raw.race)
            )
             

import datetime

def format_apod_data(apod_data):
    cur_time = datetime.datetime.now()
    cur_time = cur_time.strftime("Day: %m-%d-%Y | Time: %H:%M:%S")

    explanation = apod_data["explanation"].split(".") # makes a list of all the diff sentences, then we just want to return the first 2 sentences
    explanation = explanation[0].strip(" ") + "." + explanation[1] + "." # First we strip off all white space from before the first sentence, then we manually add periods right after each sentence.

    dict_to_return = {'date': apod_data['date'], 'title': apod_data['title'], 'url': apod_data['url'],
                      'explanation': explanation, 'logged_at': cur_time}

    return dict_to_return


TEST_DATA = {'resource': {
        'image_set': "apod"
    },
    'concept_tags': "True",
    'date': "2013-10-01",
    'title': "Earth at Night",
    'url': "http://apod.nasa.gov/apod/image/1310/velafilaments_jadescope_960.jpg",
    'explanation': 'The explosion is over but the consequences continue. About eleven thousand years ago a star in the constellation of Vela could be seen to explode. BLAH BLAH BLAH asdhjahsdhgjasd asdh.  ajsdjasdj',
    'concepts': {
        '0': "Astronomy",
        '1': "Star",
        '2': "Sun",
        '3': "Milky Way",
        '4': "Hubble Space Telescope",
        '5': "Earth",
        '6': "Nebula",
        '7': "Interstellar medium"
    }
}

TEST_DATA2 = {'resource': {
        'image_set': "apod"
    },
    'concept_tags': "True",
    'date': "2011-11-02",
    'title': "Filaments of the Vela ",
    'url': "https://apod.nasa.gov/apod/image/1707/EarthAtNight_SuomiNPP_1080.jpg",
    'explanation': "Can you find your favorite country or city?  Surprisingly, on this world-wide nightscape, city lights make this task quite possible.  Human-made lights highlight particularly developed or populated areas of the Earth's surface, including the seaboards of Europe, the eastern United States, and Japan.  Many large cities are located near rivers or oceans so that they can exchange goods cheaply by boat.  Particularly dark areas include the central parts of South America, Africa, Asia, and Australia.  The featured composite was created from images that were collected during cloud-free periods in April and October 2012 by the Suomi-NPP satellite, from a polar orbit about 824 kilometers above the surface, using its Visible Infrared Imaging Radiometer Suite (VIIRS).",
    'concepts': {
        '0': "Astronomy",
        '1': "Star",
        '2': "Sun",
        '3': "Milky Way",
        '4': "Hubble Space Telescope",
    }
}

FORMATTED_TEST_DATA = format_apod_data(TEST_DATA)
FORMATTED_TEST_DATA2 = format_apod_data(TEST_DATA2)
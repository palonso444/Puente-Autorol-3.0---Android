######### FUNCTIONS TO CONVERT JSON FILE FROM AUTOROL 3.0 INTO AN APP#########


import json



def get_scenes(path):

    with open(path) as file:
        
        jsonfile = json.load(file)

        return jsonfile ['escenas']



def get_scene(id, scenes):

    for scene in scenes:

        if scene['id'] == id:

            return scene
        


def get_intro (scenes):

    links = get_all_links(scenes)

    for scene in scenes:

        if scene['id'] not in links:

            return scene


        

################################ VARIABLES ###############################


def get_variables(scenes):

    variables = dict()

    for scene in scenes:

        for text in scene ['textos']:
        
            for condition in text['condiciones']:

                variables.update({condition['item']: 0})

        for text in scene ['textos']:
        
            for link in text ['enlaces']:

                for condition in link ['condiciones']:

                    variables.update({condition['item']: 0})

    return variables



def variables_update (variables, text):

    consequences = get_text_consequences(text)

    variables.update(consequences)

    return variables










######################################### TEXT ################################################


def get_text(scene, object = True):
    
    texts = list ()
    
    if object:
    
        for text in scene ['textos']:

            texts.append(text)

    elif not object:

        for i in range (len(scene ['textos'])):

            texts.append (scene['textos'][i]['texto'])

    return texts


def get_text_conditions (text):

    text_conditions = dict()

    for condition in text['condiciones']:

        text_conditions.update({condition['item']: int(condition['valorComparar'])})

    return text_conditions



def get_text_consequences (text):

    
    text_consequences = dict()

    for consequence in text['consecuencias']:

        text_consequences.update({consequence['item']: int(consequence['valor'])})

    return text_consequences



###################################################### LINKS #########################################


def get_all_links (scenes):

    links = set()
    
    for scene in scenes:

        for text in scene ['textos']:
        
            for link in text ['enlaces']:

                links.add(link ['destinoExito'])

    return links


def get_links (text):

    links = dict()
    
    for link in text ['enlaces']:

        links.update({link['texto']: link['destinoExito']})

    return links

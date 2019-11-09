# Implementation of the FastAPI
# Notes:
#   * Could extend with upload capability: https://fastapi.tiangolo.com/tutorial/request-files/
#

from fastapi import FastAPI, Query
import subprocess

app = FastAPI()


@app.get("/fr_to_eng/")
async def endpoint_fr_to_eng(
        q: str = Query(
            ..., # requires input, no default
            title="French text to be translated",
            description="Query string to translate from French to English.",
            min_length=2, # min length string must be
            max_length=1000 # max length string must be
        )
):
    #results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        #results.update({"q": q})
        translate_fr_to_english(q)
    return q

def translate_fr_to_english(french_text):
    '''

    :param french_text:
    :return:
    '''
    with open('fr_text.txt','w') as f:
        f.write(french_text)

    # execute the translation

    with open('run_translation_fr_eng.log', 'w') as f:
        process = subprocess.Popen(['./run_translation_fr_eng.sh'],
                                   stdout=f,
                                   stderr=f)

    #print(stdout, stderr)

    try:
        with open('back_trans_data/paraphrase/file_0_of_1.json') as f:
            print('translation from file:')
            print(f.readlines())
    except:
        print('translated file not available. Error!')




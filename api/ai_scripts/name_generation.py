from openai import OpenAI
import json
from api.settings import deepseek_url, deepseek_api_key

def generate_names(amount: str, language: str) -> dict:

    client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_url)

    # num_of_names = input("How many names to generate: ").strip()
    # language = input("What language do you want the names to come from: ").strip()


    prompt = f"Generate {amount} random Romanized full names for {language} with their meanings in JSON format. If I asked this before make all the First and Last names unique NO repeating. DO NOT give me names of historical figures. Don't respond with anything other than strict JSON. I want the response to be in this format ""{names: [{first_name: some_name , last_name: some_last_name, language: language the name originated in ,country: country the name originated in, first_name_meaning: meaning of first name, last_name_meaning: meaning of last name, gender: gender of name}]}"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You will respond with just the thing I am asking for. No fluff."},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        response_format={
            'type': 'json_object'
        }
    )

    response_json = response.choices[0].message.content

    print(response_json)
    print(type(response_json))

    if type(response_json) == str:
        response_json = json.loads(response_json)

    return response_json
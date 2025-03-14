from openai import OpenAI
import json
from settings import deepseek_api_key, deepseek_url


client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_url)

prompt = "Provide 3 Romanized Hindi full names in JSON format. The response should be a valid JSON object with a key names that contains an array of objects. Each object should have first_name, last_name, and gender fields. Ensure the response can be parsed using json.loads()."

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

print(type(json.loads(response_json)))

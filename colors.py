import openai
import json
from dotenv import dotenv_values
from IPython.display import Markdown, display  # works with jupyter notebooks


config = dotenv_values('.env')

openai.api_key = config['OPENAI_API_KEY']

def display_colors(colors):
    display(Markdown(" ".join(
        f"<span style='color: {color}>{chr(9608) * 4}</span>"
        for color in colors
    )))

def get_and_render_colors(msg):
prompt = f"""
You are a color palette generating assistant that responds to text prompts for 
color palettes.
You should generate color palettes that fit the theme, mood, or instructions in 
the prompt.
The palettes should be between 2 and 6 colors.

Q: Convert the following verbal description of a color palette into a list of 
   colors: The Mediterranean Sea
A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

Desired format: a JSON array of hexadecimal color codes

Q: Convert the following verbal description of a color palette into a list of colors: {msg}
A: 
"""

response = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    max_tokens=200
)

colors = json.loads(response['choices'][0]['text'])



display_colors(["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"])
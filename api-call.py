import json

import openai


def get_prompt(productName, productDescription, numFunct, numNonfunct):
    return f'''Below, I will give you some information about a new product and I need you to respond with a set of {numFunct} functional 
            requirements and {numNonfunct} non-functional system level requirements that could be used as a starting point for the development 
            of that product.

            The product name is {productName}. 
            This product is described as: {productDescription}
'''

def ask_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "you are an experienced requirements engineer working to the best practice stated in the INCOSE Systems Engineering Book of Knowledge (SEBoK)"},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        top_p=1,
        n=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['message']['content']
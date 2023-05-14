import openai
openai.api_key = ""

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
            {"role": "system", "content": "you are an experienced requirements engineer working to the best practice stated in the INCOSE Systems Engineering Book of Knowledge (SEBoK)"},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        top_p=1,
        n=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response
prompt = '''Below, I will give you some information about a new product and I need you to respond with a set of 20 functional 
            requirements and 20 non-functional system level requirements that could be used as a starting point for the development 
            of that product.
            
            The product name is ActivityDetect.
            The product is described as: A customer has requested a new system which takes visual input from a camera sensor and identifies unusual activity. 
            The system needs to inform the user when unusual activity is detected via a message on a PC screen
            including a timestamp and a screenshot of the camera input at the time the activity was detected. 
            The camera and PC screen are outside of the scope of the system, the system is only the software that takes the input from the camera and produces the output as a message on a software GUI
            '''

response = ask_ai(prompt)
print(response)
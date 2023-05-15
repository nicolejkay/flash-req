print("HTTP/1.0 200 OK\n")
import os
import openai
import cgi
openai.api_key = os.getenv("OPENAI_KEY")


form = cgi.FieldStorage()
test1=form["productName"].value
test2=form["productDescription"].value
test3=form["numFunct"].value
test4=form["numNonfunct"].value

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




print("<br><b>First Name</b>",f_name)
print("<br><b>Second Name</b>",s_name)
print("<br><b>Sex</b>",r1)
print("<br><b>Class</b>",my_class)
print("<br><br><br><a href=form.htm>Back to Form</a>")
import { Configuration, OpenAIApi } from 'openai';

function get_prompt(productName, productDescription, numFunct, numNonfunct) {
    return `Below, I will give you some information about a new product and I need you to respond with a set of ${numFunct} functional
            requirements and ${numNonfunct} non-functional system level requirements that could be used as a starting point for the development
            of that product.

            The product name is ${productName}.
            This product is described as: ${productDescription}
            `;
}

async function ask_ai(prompt) {
    const openai = new OpenAIApi(new Configuration({apiKey: process.env.OPENAI_KEY}));

    const completion = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [
            {"role": "system", "content": "you are an experienced requirements engineer working to the best practice stated in the INCOSE Systems Engineering Book of Knowledge (SEBoK)"},
            {"role": "user", "content": prompt},
        ],
        temperature: 0.7,
        top_p: 1,
        n: 1,
        frequency_penalty: 0,
        presence_penalty: 0
    })

    return completion.data.choices[0].message.content;
}


export default async function (request, response) {
    const body = request.body;
    console.log('Request:', body);

    const prompt = get_prompt(body.productName, body.productDescription, body.numFunct, body.numNonfunct);
    console.log('Prompt:', prompt);

    const ai = await ask_ai(prompt);
    console.log('Response:', ai);

    const output = ai;

    return response.send(output);
}


import { Configuration, OpenAIApi } from 'openai';

const role = `you are an experienced requirements engineer working to the best practice for writing system requirements
            as stated in the INCOSE Systems Engineering Book of Knowledge (SEBoK).
            You are tasked with writing system requirement documents based on system information that you will be provided.
            The requirements you write should be in simple English, be unique, verifiable,
            and provide a starting point for further system development.

            Return the requirements as a JSON object with the following headings:
            - Requirement ID (a 4 digit number starting from 0000, increasing sequentially, e.g 0000, 0001, 0002, 0003, 0004)
            - Requirement Type (will be either 'Functional' or 'Non-functional')
            - Requirement Classification (The best fit from the following list: Functional, Performance, Usability, Interface, Operational, Modes, Adaptability, Physical Constraints,
            - Design Constraints, Environmental Conditions, Logistics, Policy and Regulation, Cost and Schedule)
            - Requirement Text (the text of the requirement itself)
            - Verification Criteria (a short statement describing how it could be verified that the requirement is satisfied)
            You should only return the above with no text outside of the JSON object.  `

function get_prompt(productName, productDescription, numFunct, numNonFunct) {
    return `Below, I will give you some information about a new product and I need you to respond with a set of ${numFunct} functional
            requirements and ${numNonFunct} non-functional system level requirements that could be used as a starting point for the development
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
            {"role": "system", "content": role},
            {"role": "user", "content": prompt},
        ],
        temperature: 0.7,
        top_p: 1,
        n: 1,
        frequency_penalty: 0,
        presence_penalty: 0,
        stop: 'You:'
    })

    return completion.data.choices[0].message.content;
}


export default async function (request, response) {
    const body = request.body;
    console.log('Request:', body);

    const prompt = get_prompt(body.productName, body.productDescription, body.numFunct, body.numNonFunct);
    console.log('Prompt:', prompt);

    const ai = await ask_ai(prompt);
    console.log('Response:', ai);

    return response.json({response: ai});
}


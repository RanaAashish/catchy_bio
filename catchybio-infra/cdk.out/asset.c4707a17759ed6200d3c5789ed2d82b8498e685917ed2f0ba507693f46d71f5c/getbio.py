import os
import openai 
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import (LLMChain)
import argparse
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def main():
    parser =argparse.ArgumentParser()
    parser.add_argument("--input","-i",type=str,required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"user input: {user_input}")
    generate_bio(user_input)

def generate_bio(raw_bio):
    llm = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo-16k")
    template = """Write an impressive bio for my Tinder profile:
    context : {context}
    """

    template_prompt = template.format(context = "context")
    prompt = PromptTemplate.from_template(template_prompt)
    chain = LLMChain(llm = llm, prompt=prompt)
    input_dict = {'context':raw_bio}
    result = chain.run(input_dict)
    print(result)
    return result

if __name__ == "__main__":
    main()

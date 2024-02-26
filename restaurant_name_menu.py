from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

llm = openai(temperature=0.6)
name_prompt = PromptTemplate(
    input_variables = ["cuisine"],
    template = "Suggest fancy names for a Restaurant serving {cuisine} Food."
)

name_prompt.format(cuisine="Mexican")

menu_prompt = PromptTemplate(
    input_variables=["name"],
    templete = "Create a menu for a {name} Restaurant serving {cuisine} food. Return it as a comma seperated."
)

name_chain = LLMChain(
    llm = llm,
    prompt=name_prompt,
    output_key="name"
)

menu_chain = LLMChain(
    llm = llm,
    prompt=menu_prompt,
    output_key="menu"
)

chain = SequentialChain(
    chains=[name_chain, menu_chain],
    input_variables=["cuisine"],
    output_variables=["name", "menu"]
)

result = chain(
    {
        "cuisine" : "Mexican"
    }    
)
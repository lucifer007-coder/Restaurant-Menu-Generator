# Restaurant-Menu-Generator
This project uses the Langchain library to build a conversational chain with two LLMs. It generates a restaurant name and menu based on the cuisine type.

## Langchain Components
1. LLMChain - Connects a prompt template to an LLM to generate responses.
2. SequentialChain - Runs multiple LLMChains sequentially to form a conversation.
3. Prompt Templates - Define inputs, outputs and text format for each chain link.

## Integration with OpenAI API
The project initializes an OpenAI LLM client to power the chains. Temperature parameter controls randomness.

## Workflow
User provides "cuisine" input
First LLMChain generates a "name"
Second LLMChain takes "name" and generates a "menu"
SequentialChain runs the chains together

## Prompt Templates
Two templates are defined:
1. Name Prompt - Generates a restaurant name given cuisine type
2. Menu Prompt - Creates a comma-separated menu string from name and cuisine
Templates standardize conversation structure and variable substitution.

## Usage
The chain can be invoked from Python with cuisine as input to get structured results.
With more prompts, links and inputs - complex multi-step conversations can be built. Additional models can also be compared.
Overall, this demonstrates how Langchain provides powerful yet simple tools to construct conversational AI systems from LLMs.

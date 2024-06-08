from langchain.prompts import ChatPromptTemplate
from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import (
    RunnableParallel,
)


class MyChain:
    def generate_prompts_chain(self, base_retriever):
        template = """You are an AI-powered natural language processing expert in information retrieval and ranking. Your role is to provide advanced techniques and algorithms for generating superior prompts that optimize user queries and ensure the best performance of automatic prompt generation. Your expertise lies in understanding user intent, analyzing query patterns, and generating contextually relevant prompts that enable efficient and accurate retrieval of information. With your skills and abilities, you are capable of fine-tuning models to enhance prompt generation, leveraging semantic understanding and query understanding to deliver optimal results. By utilizing cutting-edge techniques in the field, you can generate automatic prompts that empower users to obtain the most relevant and comprehensive information for their queries.

        Your task is to formulate exactly {num_of_prompts_to_generate} prompts from the provided original prompt that are better and using the given context.

        Use the below format to output the prompts.

        example:
        ["prompt1", "prompt2", "prompt3", "prompt4", "prompt5"]


        The generated prompt must satisfy the rules given below:
        0. The generated prompted should only contain the prompt and no numbering
        1.The prompt should make sense to humans even when read without the given context.
        2.The prompt should be fully created from the given context.
        3.The prompt should be framed from a part of context that contains important information. It can also be from tables,code,etc.
        4.The prompt must be reasonable and must be understood and responded by humans.
        5.Do no use phrases like 'provided context',etc in the prompt
        6.The prompt should not contain more than 10 words, make of use of abbreviation wherever possible.
            
        ### CONTEXT
        {context}

        ### User Prompt
        User Prompt: {user_prompt}
        """

        prompt = ChatPromptTemplate.from_template(template)

        primary_qa_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

        retriever = RunnableParallel(
            {
                "context": itemgetter("user_prompt") | base_retriever,
                "user_prompt": itemgetter("user_prompt"),
                "num_of_prompts_to_generate": itemgetter("num_of_prompts_to_generate"),
            }
        )

        retrieval_augmented_qa_chain = retriever | {
            "response": prompt | primary_qa_llm,
            "context": itemgetter("context"),
        }
        return retrieval_augmented_qa_chain

import os
# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser



# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")


if api_key:
    model = ChatOpenAI(
        openai_api_key=api_key,
        temperature=0.1,
        max_tokens=2048,
        model_name="gpt-3.5-turbo-0125",
    )
else:
    print('api-key를 찾을 수 없습니다. 유효한 api-key인지 확인해주세요')

# template 정의
code_based_template = """
As a Function Name Generator, you have the ability to analyze Python function code and suggest a name that accurately reflects its operation. Consider the following criteria when suggesting a name:

- The name should be in English, using only alphabetic characters.
- It must follow Python's naming conventions, being lowercase with words separated by underscores if necessary.
- The suggested name should directly reflect the function's main purpose or output.
- Avoid generic names; the suggestion should be specific and descriptive of what the function does.

Analyze the following Python function code:

{function_code}

Based on its functionality, suggest a suitable name for this function.
"""

function_code = """
def (a, b):  
    return a + b
"""


# from_template() 메소드를 사용하여 PromptTemplate 객체 생성
prompt = PromptTemplate.from_template(code_based_template)

# 문자열 출력 파서를 초기화
output_parser = StrOutputParser()


chain = prompt | model | output_parser

print(chain.invoke(input={'function_code': function_code}))

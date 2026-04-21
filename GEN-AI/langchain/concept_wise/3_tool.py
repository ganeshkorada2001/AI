# Reference from official langchain documentation
""" 
* Tools are callable `functions` with well-defined inputs and outputs that get passed to a chat model. 
* The model decides when to invoke a tool based on the conversation context, and what input arguments to provide.

Creating Tools:
1. Basic Tool defintion:
    link: https://docs.langchain.com/oss/python/langchain/tools#basic-tool-definition
    -> "@tool" decorator is used to create the tool.
    -> Function doc string becomes the tool's descrption
    -> Type hints are required as they define the tool’s input schema
"""
# from langchain.tools import tool

# @tool
# def search_database(query: str, limit: int = 10) -> str:
#     """Search the customer database for records matching the query.

#     Args:
#         query: Search terms to look for
#         limit: Maximum number of results to return
#     """
#     return f"Found {limit} results for '{query}'"
"""
link: https://docs.langchain.com/oss/python/langchain/tools#customize-tool-properties

2. Custom tool properties
    1. tool name 
    2. tool description
        @tool("calculator", description="Performs arithmetic calculations. Use this for any math problems.")
        def calc(expression: str) -> str:
            \"""Evaluate mathematical expressions.\"""
            return str(eval(expression))
    3. advanced schema definition for input and output.
        a. pydantic or b. json shema
        @tool(args_schema=WeatherInput)

3. Access Context
    a. short-term memory
    b. long-term memory
    c. context
    d. stream writer
    e. execution info
    f. server info
4. Tool node.
"""
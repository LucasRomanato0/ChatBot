import dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

dotenv.load_dotenv()

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

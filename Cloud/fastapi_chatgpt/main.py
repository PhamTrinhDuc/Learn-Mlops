from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from loguru import logger
from utils import chat_with_llm, init_conversation

app = FastAPI()
security = HTTPBasic()

# Initialize conversation with LLM
qa = init_conversation("./products.csv")

@app.get('/metadata')
def get_metadata():
  return {"metadata": "This is a metadata endpoint."}

@app.get('/chat')
def chat(text: str): 
  logger.info(f"Chat request received with text: {text}")
  response = chat_with_llm(qa=qa, query=text)
  return {'response': response}

@app.post('/chat-auth')
def chat_auth(
  text: str,
  credentials: Annotated[HTTPBasicCredentials, Depends(security)]
  # credentials: HTTPBasicCredentials = Depends(security)
): 
  """
  credentials:	        Tên biến đầu vào (FastAPI sẽ inject vào hàm).
  Annotated[...]:       Một dạng mở rộng type hinting, cho phép kết hợp kiểu dữ liệu và xử lý đặc biệt (như Depends).
  HTTPBasicCredentials	Kiểu dữ liệu của credentials, chứa .username và .password.
  Depends(security):    Yêu cầu FastAPI tự động gọi security (được định nghĩa là security = HTTPBasic()) để lấy dữ liệu từ HTTP header, khá giống decorator @Autowired trong Spring.

  Cách hoạt động:
  1. Khi có request đến API:
  2. FastAPI nhìn vào credentials: Annotated[...]
  3. Nó hiểu: "À, cần gọi Depends(security) để lấy credentials"
  4. Depends(security) gọi hàm xác thực HTTP Basic → lấy ra username, password
  5. Đưa kết quả vào biến credentials (kiểu HTTPBasicCredentials)
  """

  if credentials.username != "admin" or credentials.password != "password":
    logger.warning("Unauthorized access attempt.")
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid credentials",
      headers={"WWW-Authenticate": "Basic"},
    )
  logger.info(f"Chat request received with text: {text} and credentials: {credentials.username}")
  response = chat_with_llm(qa=qa, query=text)
  return {'response': response}
  

if __name__ == "__main__":
  import uvicorn
  logger.info("Starting FastAPI server...")
  uvicorn.run(app, host="0.0.0.0", port=8000)
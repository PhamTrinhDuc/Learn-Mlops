# test balancing 
# => stress test: test hệ thống chịu được bao nhiêu request (giới hạn của sever)
# => load test: dưới 1 lượng request nhất định, hệ thống có behavior như thế nào

from locust import HttpUser, task, between
from loguru import logger

class ModelUser(HttpUser):
  # Wait between 1 and 3 seconds between requrests
  wait_time = between(1, 3)

  def on_start(self):
      logger.info("Load your model here")

  @task
  def predict(self):
      logger.info("Sending POST requests!")
      image = open('images/receipt.jpg', 'rb')
      files = {'file': image}
      self.client.post(
          "/ocr/cache",
          files=files,
      )
      # logger.info("Sending GET requests!")
      # self.client.get(
      #     "/simple",
      # )

# Chạy locust để load test:  
# 1. Định nghĩa locustfile.py
# 2. Chạy lệnh sau trong terminal: locust
# 3. Trong file locustfile.py, định nghĩa class ModelUser kế thừa từ HttpUser
# 4. Đinh nghĩa method có decorator @task bên trong chỉ định enpoint sử dụng 
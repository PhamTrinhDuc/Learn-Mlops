### WEBSOCKET

WebSocket là một giao thức giúp giao tiếp 2 chiều (full-duplex) giữa client (trình duyệt) và server theo thời gian thực. Khác với HTTP (phải request mới có response), WebSocket cho phép giữ kết nối liên tục, server có thể gửi dữ liệu bất cứ lúc nào mà không cần client yêu cầu lại.

So sánh nhanh WebSocket vs HTTP:
Đặc điểm	              HTTP	                              WebSocket
Kiểu kết nối	  Một chiều (request → response)	    Hai chiều (full-duplex)
Giữ kết nối	    Không	                              Có (kết nối liên tục)
Tốc độ	        Chậm hơn do mỗi lần gửi lại header	Nhanh hơn, không cần gửi lại header
Dùng cho	      Web bình thường	                    App real-time (chat, game, stock...)



# CS336.L12.KHCL
- Đồ án môn học: Truy vấn thông tin đa phương tiện
# Image Search Engine Based On Caption
- Tên đề tài: Xây dựng hệ thống tìm kiếm ảnh sử dụng mô tả ( Image Search Base On Caption )
  + Input: Một câu mô tả ảnh
  + Output: Các hình ảnh liên quan với câu mô tả
  
## Ngôn ngữ sử dụng
- python 3


## Bài toán image captioning
- Training một model có khả năng tạo ra câu mô tả cho hình ảnh đầu vào

### Download the Flickr8k dataset
https://www.kaggle.com/adityajn105/flickr8k?fbclid=IwAR0_e4CGS5YYK0IKpcnrp_4u3PaOaliBp5OLxM7KnlMbfbOsbMzd63mo5ME

### Mô tả các thư mục
- Flicker8k_Dataset: Chứa các hình ảnh
- Flickr8k_text: Chứa các câu mô tả ảnh dùng cho việc traning model

### Mô tả các scripts
- Text_Preprocess.py: Chuẩn bị dữ liệu cho training 

- Loader.py: Chứa các hàm xử lý dữ liệu 

- TF_IDF_score.py: Dùng để tính toán và truy xuất hình ảnh


## Bài toán truy vấn ảnh
- Sử dụng mô hình Vector Space Model để lập chỉ mục truy vấn hình ảnh

## Running the tests

- Chạy trên local:
```
1. Cài đặt máy chủ ảo xampp
2. Mở browser và truy cập địa chỉ: http://localhost/uploads/index.php
```


## Authors

* **Võ Gia Bảo** - *18520502*
* **Nguyễn Đức Hà** - *18520689*
* **Trần Lê Duy** - *18520674*
* **Nguyễn Trung Hiếu** - *18520751*

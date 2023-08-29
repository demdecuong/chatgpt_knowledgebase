##  Langchain + ChatGPT + FAISS  

Integrate ChatGPT to internal KnowledgeBase effectively.
Requirements:  
- Medium corpus of knowledge base
- Easy to maintin when the Knowledge base is updated through time monthly
- Control the precision/factness of the output
- Handling invalid outputs
- Compare to other methods (BM25, semantic search)

### Installation
Python: 3.9
```
pip install -r requirements.txt
```


#### Usage
```
python main.py
```
Expected output: query = "Sản phẩm này có những gì cần lưu ý"
```
Sản phẩm Bảo Hiểm Bổ Sung có những điều cần lưu ý sau:

1. Phí bảo hiểm có thể thay đổi tùy thuộc vào tuổi, chương trình và quyền lợi của người được bảo hiểm tại ngày kỷ niệm hợp đồng. Phí bảo hiểm cũng có thể thay đổi theo sự chấp thuận của Bộ Tài chính.

2. Để đảm bảo quyền lợi bảo hiểm, khách hàng cần đóng đầy đủ và đúng hạn các khoản phí bảo hiểm, ngay cả khi không nhận được thông báo nhắc đóng phí.

3. Định kỳ đóng phí của Bảo Hiểm Bổ Sung sẽ áp dụng cho định kỳ đóng phí của hợp đồng bảo hiểm chính. Khi có sự thay đổi về định kỳ đóng phí của hợp đồng bảo hiểm chính, định kỳ đóng phí của Bảo Hiểm Bổ Sung cũng sẽ thay đổi tương ứng.

4. Khách hàng được gia hạn đóng phí bảo hiểm trong vòng 60 ngày kể từ ngày đến hạn đóng phí. Trong thời gian này, quyền lợi bảo hiểm vẫn được đảm bảo.

5. Thời hạn của sản phẩm Bảo Hiểm Bổ Sung sẽ được xác định trong hợp đồng bảo hiểm.
```
tạo trước thư mục result, vì hàm open mode w không tự tạo dc.
có r thì thôi.

1. đầu tiên chạy file create key.py
nó sẽ tạo 2 file json trong /result, là public key và private key.

2. tiếp theo chạy encrypt.py
nó đọc vào file public key.json và data.txt, output là file /result/encrypted_data.txt 

3. cuối cùng chạy decrypt.py
nó đọc vào file private_key.json và data.txt, output là file /result/decrypted_data.txt
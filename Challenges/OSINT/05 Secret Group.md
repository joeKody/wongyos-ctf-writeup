# Secret Group
จากไฟล์ข้อมูลลับที่จัดเก็บใน Mega นั้นยังมีข้อมูลของกลุ่มลับซ่อนอยู่ภายในไฟล์นั้น แต่ไฟล์ดังกล่าวติดรหัสผ่าน จงพยายามเปิดไฟล์และค้นหากลุ่มกลับดังกล่าวให้ได้ แล้วจะเจอกับ flag ที่ต้องการ

HINT : รหัสผ่านของไฟล์นี้มี 7 หลัก เป็นอักษรภาษาอังกฤษพิมพ์เล็กทั้งหมด โดยหลักสุดท้ายจบด้วยตัว "a" ส่วนอีก 6 หลักที่เหลือเกิดจากการสลับอักษร 6 ตัว ได้แก่ "acelmr" และ อักษรทั้ง 6 ตัวนี้เมื่อสลับอย่างถูกต้องจะได้คำที่มีความหมาย และเมื่อนำไปต่อกับ "a" ก็จะได้รหัสผ่านของไฟล์

<details>
    <summary>Solution</summary>
    
- ผมโหลดไฟล์(เปลี่ยนชื่อเป็น `file.zip`) และใช้คำสั่งสองอย่างเพื่อ bruteforce หา password
```
zip2john file.zip > hash
john hash
```
![bruteforce](https://github.com/joeKody/wongyos-ctf-writeup/assets/115410150/cfc076b3-83ab-402d-873a-5141381987e9)

- เมื่อได้ password ก็แตกไฟล์จะได้ไฟล์ txt ซึ่งคือลิงก์กลุ่มไลน์
![data](https://github.com/joeKody/wongyos-ctf-writeup/assets/115410150/ed820e05-e6d6-4d19-a734-095d9d978e4b)
 
- flag จะอยู่ใน Note ของกลุ่มนี้!

</details>
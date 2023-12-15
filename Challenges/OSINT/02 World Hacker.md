# World Hacker

เจ้าหน้าที่ตำรวจได้รับการรายงานมาว่าสมาชิกคนหนึ่งในแฮกเกอร์กลุ่มนี้ประกอบอาชีพขายดอกไม้ และเรียนจบสาขาวิทยาการคอมพิวเตอร์ มีความรู้เรื่องคอมพิวเตอร์เป็นอย่างดี โดยเขาซ่อน flag เอาไว้บนโซเชียลมีเดียแห่งหนึ่งพร้อมกับข้อความลับที่ถูกเข้ารหัสเอาไว้ตามที่กำหนดให้ จงหาเขาคนนั้นให้เจอ

```
-.- --- -. --. -.- .- .--. .- -.
.--. .- -. -.-- .- -.. . .
```

<details>
    <summary>Solution</summary>
    
- ข้อนี้ได้ให้ Morse code เรามา ผมจึงไปถอดมาได้คำว่า `KONGKAPAN PANYADEE`  
![morse_decode](https://github.com/joeKody/wongyos-ctf-writeup/assets/115410150/5ef2133a-93b2-4892-a776-be93e4ab61da)

- หลังจากนั้นนำชื่อนี้ไปเสิร์ชจะเจอกับโปรไฟล์ Facebook หนึ่ง  
![gg_search](https://github.com/joeKody/wongyos-ctf-writeup/assets/115410150/0ab6e7a4-2766-49c5-ae45-dabc0984387b)

- หากเข้าไปดูในหน้า About page และลองดูใน Details ก็จะเจอกับ flag ครับ!  
![image](https://github.com/joeKody/wongyos-ctf-writeup/assets/115410150/8489afbe-14e3-4c8f-bac5-316d4a929d8f)

</details>
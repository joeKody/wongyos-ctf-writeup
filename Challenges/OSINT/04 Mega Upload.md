# Mega Upload

แฮกเกอร์ Kongkapan Panyadee ยังได้โพสต์ลิงค์จัดเก็บไฟล์ข้อมูลที่มี flag ซ่อนอยู่ ซึ่งไฟล์ดังกล่าวอยู่ในระบบ Cloud ที่ชื่อ Mega แต่อย่างไรก็ตามชื่อลิงค์ดังกล่าวมีอักษรตัวสุดท้ายที่ขาดหายไปทำให้เปิดไม่ได้ ซึ่งอาจจะเป็นตัวเลขหรือตัวอักษรภาษาอังกฤษอย่างใดอย่างหนึ่ง จงพยายามเข้าถึงไฟล์ข้อมูลลับจากลิงค์ดังกล่าวให้ได้

<details>
    <summary>Solution</summary>
    
- ตามที่โจทย์บอกว่ามีตัวอักษรหายไปหนึ่งตัวใน URL นี้
```
https://mega.nz/file/g8UEyZ4Y#snPyV3h-Ga62ufx0c95QXPFnp96AvyVGhHrdsVLva4
```
![mega](https://github.com/joeKody/wongyos-ctf-writeup/assets/115410150/46199645-8bc5-4c67-b42f-4b93c4ca027d)

- ผมเลยลองทุกเอาตัวอักษรทุกตัว ต่อหลังดูทีละตัวซึ่งก็เจอกับ URL ที่ถูกต้อง และพบกับ flag!
![flag](https://github.com/joeKody/wongyos-ctf-writeup/assets/115410150/30601183-62bb-40d5-9e2c-10ecd93909ec)


</details>
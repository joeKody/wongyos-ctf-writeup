## Love Emoji [81 pts]

ฉันรักอิโมจิ เพราะอิโมจิมี Flag

<details>
    <summary>Solution</summary>
    
- TLDR : `UNICODE -> ASCII`
- นำค่า decimal ของ emoji มาแปลงเป็น ascii โดยเทียบตัวแรกเป็น f ตัวที่สองเป็น l จะได้โค้ด python ดังนี้
```py
flag = "😶😼😱😷🙋😇😴😈😈😂😅😴😀😆😈😳😳😶😳😁😁😵😁😵😆😲😆😆😀😄😲😴😵😈😇😅😂🙍"
for i in flag:
    diff = ord(flag[0]) - ord('f')
    current = ord(i) - diff
    print(chr(current), end="")
```
  
</details>
# Week5
---
## 要求三：SQL CRUD

- 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。<br>
接著繼續新增⾄少 4 筆隨意的資料。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/3-1.JPG)
- 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/3-2.JPG)
- 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/3-3.JPG)
- 使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，<br>
並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
![image](https://github.com/rororoisme/WeHelp/blob/main/img/3-4.JPG)
- 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/3-5.JPG)
- 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/3-6.JPG)
- 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/3-7.JPG)
---
## 要求四：SQL Aggregate Functions

- 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/4-1.JPG)
- 取得 member 資料表中，所有會員 follower_count 欄位的總和。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/4-2.JPG)
- 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/4-3.JPG)
---
## 要求五：SQL JOIN

- 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/5-1.JPG)
- 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留⾔，資料中須包含留⾔者的姓名。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/5-2.JPG)
- 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中
欄位 username 是 test 的所有留⾔平均按讚數。
![image](https://github.com/rororoisme/WeHelp/blob/main/img/5-3.JPG)

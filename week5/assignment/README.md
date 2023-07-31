
# Task 2
!(img)[https://github.com/codeotter0201/bootcamp/blob/master/week5/assignment/src/task2_create_member_table.png]
### login
`mysql -u root -p`

### create database
`CREATE DATABASE website;`

### choose database
`USE website;`

### create member table
```mysql
CREATE TABLE member (
  id bigint PRIMARY KEY AUTO_INCREMENT,
  name varchar(255) NOT NULL,
  username varchar(255) NOT NULL,
  password varchar(255) NOT NULL,
  follower_count int unsigned NOT NULL DEFAULT 0,
  time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

# Task 3
## ● 使用 INSERT 指令新增一筆資料到 member 資料表中,這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
```mysql
INSERT INTO member (name, username, password, follower_count, time)
VALUES ('test', 'test', 'test', 10, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR)),
       ('John Doe', 'johndoe', 'password1', 10, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR)),
       ('Jane Smith', 'janesmith', 'password2', 5, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR)),
       ('Alice Johnson', 'alicejohnson', 'password3', 2, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR)),
       ('Bob Williams', 'bobwilliams', 'password4', 7, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR));
```

## ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
`SELECT * FROM member;`

## ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料,並按照 time 欄位,由近到遠排序。
`SELECT * FROM member ORDER BY time DESC;`

## ● 使用 SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料,並按照 time 欄位,由近到遠排序。( 並非編號 2、3、4 的資料,而是排序後的第 2 ~ 4 筆資料 )
`SELECT * FROM member ORDER BY time DESC LIMIT 1, 3;`

## ● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
`SELECT * FROM member WHERE username = 'test';`

## ● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
`SELECT * FROM member WHERE username = 'test' and password = 'test';`

## ● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料,將資料中的 name 欄位改成 test2。
`UPDATE member SET name = 'test2' WHERE username = 'test';`

# Task 4
## ● 取得 member 資料表中,總共有幾筆資料 ( 幾位會員 )。
`SELECT COUNT(*) FROM member;`

## ● 取得 member 資料表中,所有會員 follower_count 欄位的總和。
`SELECT SUM(follower_count) FROM member;`

## ● 取得 member 資料表中,所有會員 follower_count 欄位的平均數。
`SELECT AVG(follower_count) FROM member;`

# Task 5
## create message table
```mysql
CREATE TABLE message (
  id bigint PRIMARY KEY AUTO_INCREMENT,
  member_id bigint NOT NULL,
  content varchar(255) NOT NULL,
  like_count int unsigned NOT NULL DEFAULT 0,
  time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (member_id) REFERENCES member(id)
);
```

## insert messages
```mysql
INSERT INTO message (member_id, content, like_count, time)
SELECT id, CONCAT('Message ', FLOOR(RAND() * 1000)), FLOOR(RAND() * 1000), DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 100) + 1 HOUR)
FROM member;
```

```mysql
INSERT INTO message (member_id, content, like_count, time)
VALUES (FLOOR(RAND() * 5) + 1, 'content1', FLOOR(RAND() * 1000) + 1, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR)),
  (FLOOR(RAND() * 5) + 1, 'content2', FLOOR(RAND() * 1000) + 1, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR)),
  (FLOOR(RAND() * 5) + 1, 'content3', FLOOR(RAND() * 1000) + 1, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR)),
  (FLOOR(RAND() * 5) + 1, 'content4', FLOOR(RAND() * 1000) + 1, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR)),
  (FLOOR(RAND() * 5) + 1, 'content5', FLOOR(RAND() * 1000) + 1, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR)),
  (FLOOR(RAND() * 5) + 1, 'content6', FLOOR(RAND() * 1000) + 1, DATE_ADD(NOW(), INTERVAL FLOOR(RAND() * 12) + 1 HOUR));
```

## ● 使用 SELECT 搭配 JOIN 語法,取得所有留言,結果須包含留言者的姓名。
```mysql
SELECT m.*, mem.name AS member_name
FROM message AS m
JOIN member AS mem ON m.member_id = mem.id;
```

## ● 使用 SELECT 搭配 JOIN 語法,取得 member 資料表中欄位 username 是 test 的所有留言,資料中須包含留言者的姓名。
```mysql
SELECT m.*, mem.name AS member_name
FROM message AS m
JOIN member AS mem ON m.member_id = mem.id
WHERE mem.username = 'test';
```


## ● 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法,取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
```mysql
SELECT AVG(m.like_count) AS average_likes
FROM message AS m
JOIN member AS mem ON m.member_id = mem.id
WHERE mem.username = 'test';
```

# export data.sql
`mysqldump -u root -p website > data.sql`

# import data.sql
`mysqldump -u root -p -e create database testimport;`
`mysql -u root -p test_import < data.sql`
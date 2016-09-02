# Netease-comb CLI 

```
root@debian-test-master:~/comb_client# ./comb.py --help
Usage: comb.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  app-image-list
  container-delete
  container-flow
  container-image-list
  container-list
  container-restart
  container-show
  container-to-image
  repositories-list
  repositories-show
root@debian-test-master:~/comb_client# 
```


## 列出所有镜像

```
root@debian-test-master:~/comb_client# ./comb.py app-image-list
+-------+------------+--------+
|    id | name       | tag    |
|-------+------------+--------|
| 22568 | minimal    | latest |
| 35630 | myss2-0528 | latest |
| 30656 | myss       | latest |
| 26413 | nagios     | v1     |
| 22567 | aas        | latest |
| 1     | tomcat     | 7.0.62 |
| 5     | php        | 5.5    |
| 6     | nodejs     | 0.12.2 |
| 7     | python     | 2.7    |
| 9     | ruby       | 1.9    |
| 26369 | tomcat_apm | latest |
+-------+------------+--------+
root@debian-test-master:~/comb_client# 
```

## 列出所有容器

```
root@debian-test-master:~/comb_client# ./comb.py  container-list
+--------+------------+-------------+---------------+------------+
|     id | name       | status      | public_ip     |   image_id |
|--------+------------+-------------+---------------+------------|
| 630831 | testNagios | create_succ | 59.111.91.56  | 26413      |
| 628306 | test       | create_succ | 59.111.91.23  | 21697      |
| 193887 | myss2      | create_succ | 59.111.72.128 | 30656      |
+--------+------------+-------------+---------------+------------+
root@debian-test-master:~/comb_client# 
```

## 查询容器信息

```
root@debian-test-master:~/comb_client# ./comb.py  container-show 630831
+-----------+--------------+
| Field     | Value        |
|-----------+--------------|
| id        | 630831       |
| name      | testNagios   |
| status    | create_succ  |
| bandwidth | 100          |
| public_ip | 59.111.91.56 |
| image_id  | 26413        |
+-----------+--------------+
root@debian-test-master:~/comb_client# 
```

## 查询已用的流量

```
root@debian-test-master:~/comb_client# ./comb.py  container-flow 630831
+---------------------+---------+
| Field               | Value   |
|---------------------+---------|
| container_up_flow   | 0.00B   |
| container_down_flow | 0.00B   |
+---------------------+---------+
root@debian-test-master:~/comb_client# ./comb.py  container-flow 193887
+---------------------+---------+
| Field               | Value   |
|---------------------+---------|
| container_up_flow   | 18.61GB |
| container_down_flow | 30.66GB |
+---------------------+---------+
root@debian-test-master:~/comb_client# 
```


## 重启容器

```
root@debian-test-master:~/comb_client# ./comb.py  container-restart  630831
root@debian-test-master:~/comb_client# ./comb.py  container-list
+--------+------------+--------------+---------------+------------+
|     id | name       | status       | public_ip     |   image_id |
|--------+------------+--------------+---------------+------------|
| 630831 | testNagios | restart_succ | 59.111.91.56  | 26413      |
| 628306 | test       | create_succ  | 59.111.91.23  | 21697      |
| 193887 | myss2      | create_succ  | 59.111.72.128 | 30656      |
+--------+------------+--------------+---------------+------------+
root@debian-test-master:~/comb_client# 
```


## 删除容器

```
root@debian-test-master:~/comb_client# ./comb.py  container-delete 630831 
root@debian-test-master:~/comb_client# ./comb.py  container-list
+--------+--------+-------------+---------------+------------+
|     id | name   | status      | public_ip     |   image_id |
|--------+--------+-------------+---------------+------------|
| 628306 | test   | create_succ | 59.111.91.23  | 21697      |
| 193887 | myss2  | create_succ | 59.111.72.128 | 30656      |
+--------+--------+-------------+---------------+------------+
root@debian-test-master:~/comb_client# 
```


## 容器镜像列表

```
root@debian-test-master:~/comb_client# ./comb.py   container-image-list
+-------+------------+--------------+
|    id | name       | tag          |
|-------+------------+--------------|
| 22568 | minimal    | latest       |
| 35630 | myss2-0528 | latest       |
| 30656 | myss       | latest       |
| 26413 | nagios     | v1           |
| 22567 | aas        | latest       |
| 21640 | mongodb    | 3.2.0        |
| 21699 | postgres   | 9.5.1        |
| 21697 | centos     | 6.5          |
| 10005 | centos     | 6.7          |
| 27066 | centos     | 7-common     |
| 20762 | centos     | 7.0          |
| 20837 | tomcat     | 7.0.28       |
| 21651 | nodejs     | 5.7.0        |
| 10029 | debian     | 7.8          |
| 27032 | debian     | 7.9          |
| 27033 | debian     | 7.9-common   |
| 20182 | javaweb    | latest       |
| 20838 | django     | 1.9.1        |
| 20836 | jdk        | 1.7.0_03     |
| 20834 | jenkins    | 1.642.1      |
| 20175 | LAMP       | latest       |
| 10037 | mysql      | 5.6          |
| 20835 | nginx      | 1.2.1        |
| 10036 | redis      | 2.8.4        |
| 1003  | ubuntu     | 14.04        |
| 27062 | ubuntu     | 14.04-common |
| 20769 | ubuntu     | 15.04        |
| 20770 | ubuntu     | 16.04        |
| 38664 | wordpress  | 4.5.2        |
+-------+------------+--------------+
root@debian-test-master:~/comb_client# 
```


## 镜像列表

```
root@debian-test-master:~/comb_client# ./comb.py repositories-list
+-----------+-------------+----------------------+
|   repo_id | repo_name   | created_at           |
|-----------+-------------+----------------------|
| 2095      | minimal     | 2016-03-18T09:02:07Z |
| 18312     | myss2-0528  | 2016-05-28T14:41:13Z |
| 10671     | myss        | 2016-05-06T13:21:38Z |
| 5331      | nagios      | 2016-04-15T03:09:27Z |
| 2093      | aas         | 2016-03-18T08:56:51Z |
+-----------+-------------+----------------------+
```

## 查询镜像详情

```
root@debian-test-master:~/comb_client# ./comb.py repositories-show 5331
+-------------+----------------------+
| Field       | Value                |
|-------------+----------------------|
| repo_id     | 5331                 |
| repo_name   | nagios               |
| user_name   | fcyiqiao             |
| open_level  | 1                    |
| detail_desc |                      |
| created_at  | 2016-04-15T03:09:27Z |
| updated_at  | 2016-04-15T04:47:44Z |
+-------------+----------------------+
```


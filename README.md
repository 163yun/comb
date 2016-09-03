
# Netease-comb CLI 

```
root@debian-test-master:~/comb_client# ./comb.py   
Usage: comb.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  app-image-list
  container-create
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

## 安装

```
git clone git://github.com/mooz/percol.git
cd comb
```

### 依赖

```
click
tabulate
```

可以这样安装依赖

```
pip install click
pip install tabulate
```



## 使用

### 认证

蜂巢 API 需要使用 API Token 来发起 API 请求。 请到 https://c.163.com 页面登陆到你的账户，查看你的 Access Key 和 Access Secret。

然后编辑你的 `auth.conf` 文件，将`ACCESS_KEY`  和 `ACCESS_SECRET` 替换为你的即可。

```
[DEFAULT]
COMB_OPENAPI = https://open.c.163.com
ACCESS_KEY = 07ed767760f74d8a868071144d1048e8
ACCESS_SECRET = d965faa27f794e588c412ad90b6340fc
```


### 列出所有镜像

```
root@debian-test-master:~/comb_client# ./comb.py app-image-list
+-------+------------+--------+----------+
| id    | name       | tag    | weight   |
|-------+------------+--------+----------|
| 22568 | minimal    | latest | 0        |
| 35630 | myss2-0528 | latest | 1000     |
| 30656 | myss       | latest | 0        |
| 26413 | nagios     | v1     | 0        |
| 22567 | aas        | latest | 0        |
| 1     | tomcat     | 7.0.62 | 1000     |
| 5     | php        | 5.5    | 1000     |
| 6     | nodejs     | 0.12.2 | 1000     |
| 7     | python     | 2.7    | 1000     |
| 9     | ruby       | 1.9    | 1000     |
| 26369 | tomcat_apm | latest | 0        |
+-------+------------+--------+----------+

```

### 创建容器


```
root@debian-test-master:~/comb_client# ./comb.py container-create --charge_type 1 --spec_id 1 --image_type 1 --image_id 10005 --name testNew

{"charge_type": "1", "image_id": "10005", "bandwidth": "", "name": "testNew", "use_public_network": "", "image_type": "1", "network_charge_type": "", "spec_id": "1", "desc": ""}
{u'id': 631746}  

root@debian-test-master:~/comb_client# ./comb.py   container-list
+--------+---------+-------------+---------------+------------+
| id     | name    | status      | public_ip     | image_id   |
|--------+---------+-------------+---------------+------------|
| 631746 | testNew | create_succ | 59.111.91.67  | 10005      |
| 628306 | test    | create_succ | 59.111.91.23  | 21697      |
| 193887 | myss2   | create_succ | 59.111.72.128 | 30656      |
+--------+---------+-------------+---------------+------------+

```


### 列出所有容器

```
root@debian-test-master:~/comb_client# ./comb.py  container-list
+--------+---------+-------------+---------------+------------+
| id     | name    | status      | public_ip     | image_id   |
|--------+---------+-------------+---------------+------------|
| 631746 | testNew | create_succ | 59.111.91.67  | 10005      |
| 628306 | test    | create_succ | 59.111.91.23  | 21697      |
| 193887 | myss2   | create_succ | 59.111.72.128 | 30656      |
+--------+---------+-------------+---------------+------------+

```

### 查询容器信息

```
root@debian-test-master:~/comb_client# ./comb.py  container-show 631746
+---------------------+----------------------+
| Field               | Value                |
|---------------------+----------------------|
| id                  | 631746               |
| bandwidth           | 100                  |
| charge_type         | 1                    |
| created_at          | 2016-09-02T06:41:48Z |
| desc                |                      |
| env_var             |                      |
| image_id            | 10005                |
| name                | testNew              |
| network_charge_type | 2                    |
| private_ip          | 10.173.32.82         |
| public_ip           | 59.111.91.67         |
| replicas            | 1                    |
| spec_id             | 1                    |
| ssh_key_ids         |                      |
| status              | create_succ          |
| updated_at          | 2016-09-02T06:42:22Z |
| use_public_network  | 1                    |
+---------------------+----------------------+
```

### 查询已用的流量

```
root@debian-test-master:~/comb_client# ./comb.py  container-flow  631746
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
```


### 重启容器

```
root@debian-test-master:~/comb_client# ./comb.py  container-restart 631746
root@debian-test-master:~/comb_client# ./comb.py  container-list
+--------+---------+--------------+---------------+------------+
| id     | name    | status       | public_ip     | image_id   |
|--------+---------+--------------+---------------+------------|
| 631746 | testNew | restart_succ | 59.111.91.67  | 10005      |
| 628306 | test    | create_succ  | 59.111.91.23  | 21697      |
| 193887 | myss2   | create_succ  | 59.111.72.128 | 30656      |
+--------+---------+--------------+---------------+------------+
```


### 删除容器

```
root@debian-test-master:~/comb_client# ./comb.py  container-delete 631746
root@debian-test-master:~/comb_client# ./comb.py  container-list
+--------+--------+-------------+---------------+------------+
| id     | name   | status      | public_ip     | image_id   |
|--------+--------+-------------+---------------+------------|
| 628306 | test   | create_succ | 59.111.91.23  | 21697      |
| 193887 | myss2  | create_succ | 59.111.72.128 | 30656      |
+--------+--------+-------------+---------------+------------+
```


### 容器镜像列表

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
```


### 镜像列表

```
root@debian-test-master:~/comb_client# ./comb.py repositories-list

+-----------+-------------+-------------+--------------+-------------+----------------------+
| repo_id   | user_name   | repo_name   | open_level   | tag_count   | updated_at           |
|-----------+-------------+-------------+--------------+-------------+----------------------|
| 2095      | fcyiqiao    | minimal     | 1            | 1           | 2016-06-03T09:59:04Z |
| 18312     | fcyiqiao    | myss2-0528  | 0            | 1           | 2016-05-28T14:43:05Z |
| 10671     | fcyiqiao    | myss        | 0            | 1           | 2016-05-06T13:23:21Z |
| 5331      | fcyiqiao    | nagios      | 1            | 1           | 2016-04-15T04:47:44Z |
| 2093      | fcyiqiao    | aas         | 0            | 1           | 2016-03-18T08:57:53Z |
+-----------+-------------+-------------+--------------+-------------+----------------------+
```

### 查询镜像详情

```
root@debian-test-master:~/comb_client# ./comb.py repositories-show 5331
+-------------+----------------------+
| Field       | Value                |
|-------------+----------------------|
| repo_id     | 5331                 |
| user_name   | fcyiqiao             |
| repo_name   | nagios               |
| open_level  | 1                    |
| base_desc   |                      |
| detail_desc |                      |
| tag_count   | 1                    |
| created_at  | 2016-04-15T03:09:27Z |
| updated_at  | 2016-04-15T04:47:44Z |
+-------------+----------------------+
```

## tips

当使用 comb 管理大量容器时，可以通过shell循环实现容器资源的批量操作



### 批量创建

```
root@debian-test-master:~/comb_client# for i in $(seq 1 5); do ./comb.py container-create --charge_type 1 --spec_id 1 --image_type 1 --image_id 10005 --name testCentos$i ; done


root@debian-test-master:~/comb_client# ./comb.py container-list
+--------+-------------+-------------+---------------+------------+
| id     | name        | status      | public_ip     | image_id   |
|--------+-------------+-------------+---------------+------------|
| 635717 | testCentos5 | create_succ | 59.111.91.75  | 10005      |
| 635716 | testCentos4 | create_succ | 59.111.91.74  | 10005      |
| 635715 | testCentos3 | create_succ | 59.111.91.73  | 10005      |
| 635714 | testCentos2 | create_succ | 59.111.91.72  | 10005      |
| 635713 | testCentos1 | create_succ | 59.111.91.71  | 10005      |
| 634664 | testNew2    | create_succ | 59.111.91.69  | 10005      |
| 634663 | testNew1    | create_succ | 59.111.91.68  | 10005      |
| 628306 | test        | create_succ | 59.111.91.23  | 21697      |
| 193887 | myss2       | create_succ | 59.111.72.128 | 30656      |
+--------+-------------+-------------+---------------+------------+
```


### 批量删除名字中含有testNew的容器

```
root@debian-test-master:~/comb_client# ./comb.py container-list |grep testNew |awk '{print $2}' | xargs -n 1 ./comb.py container-delete 

root@debian-test-master:~/comb_client# ./comb.py container-list
+--------+-------------+-------------+---------------+------------+
| id     | name        | status      | public_ip     | image_id   |
|--------+-------------+-------------+---------------+------------|
| 635717 | testCentos5 | create_succ | 59.111.91.75  | 10005      |
| 635716 | testCentos4 | create_succ | 59.111.91.74  | 10005      |
| 635715 | testCentos3 | create_succ | 59.111.91.73  | 10005      |
| 635714 | testCentos2 | create_succ | 59.111.91.72  | 10005      |
| 635713 | testCentos1 | create_succ | 59.111.91.71  | 10005      |
| 628306 | test        | create_succ | 59.111.91.23  | 21697      |
| 193887 | myss2       | create_succ | 59.111.72.128 | 30656      |
+--------+-------------+-------------+---------------+------------+
```


### 批量删除所有使用centos 6.7 镜像创建的容器

```
root@debian-test-master:~/comb_client# ./comb.py container-list |grep 10005  |awk '{print $2}' | xargs -n 1 ./comb.py container-delete 
root@debian-test-master:~/comb_client# ./comb.py container-list
+--------+--------+-------------+---------------+------------+
| id     | name   | status      | public_ip     | image_id   |
|--------+--------+-------------+---------------+------------|
| 628306 | test   | create_succ | 59.111.91.23  | 21697      |
| 193887 | myss2  | create_succ | 59.111.72.128 | 30656      |
+--------+--------+-------------+---------------+------------+

```



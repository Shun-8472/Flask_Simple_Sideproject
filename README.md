# **Simple Project**

###### Fast Learning Flask

Use technology:
```
- python
- Flask
- Redis
- MySQL
```

Next Step:
```
- Data Sharding (Horizontal Scaling)
```

System Design:
![image](images/system_design.png)

API:

| Method   | URL                                      | Description                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `POST`   | `/users/SignIn`                          | User SignIn.                             |
| `POST`   | `/users/SignUp`                          | User SignUp.                             |
| `POST`   | `/users/{userId}`                        | User update information.                 |
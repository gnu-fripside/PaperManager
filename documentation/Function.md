# Some Essential Functions of PaperManager
-------------

## user_register

- arguments

| name    | type           | means                          |
| ------  | ------         | ------                         |
| request | django request | user register request          |

- request structure

| name     | type   | means                      |
| ------   | ------ | ------                     |
| username | str    | user name to be registered |
| password | str    | user password              |
| email    | str    | user email                 |

- return value

| name     | type         | means                                 |
| ------   | ------       | ------                                |
| response | JsonResponse | the result of this register operation |

- return dict structure

| name      | type   | means         |
| ------    | ------ | ------        |
| error_num | int    | error number  |
| msg       | str    | error message |

- error_num table

|  value | means                              |
| ------ | ------                             |
|      0 | succeed                            |
|      1 | this user name has been registered |

## user_login

- arguments

| name    | type           | means                          |
| ------  | ------         | ------                         |
| request | django request | user login request             |

- request structure

| name     | type   | means                      |
| ------   | ------ | ------                     |
| username | str    | user name to be login      |
| password | str    | user password              |

- return value

| name     | type         | means                                 |
| ------   | ------       | ------                                |
| response | JsonResponse | the result of this register operation |

- return dict structure

| name      | type   | means                       |
| ------    | ------ | ------                      |
| error_num | int    | error number                |
| msg       | str    | error message               |
| cookie    | str    | when succeed, cookie exists |

- error_num table

|  value | means                         |
| ------ | ------                        |
|      0 | succeed                       |
|      1 | wrong password                |
|      2 | this user name does not exist |

## user_logout

- arguments

| name    | type           | means               |
|---------|----------------|---------------------|
| request | django_request | user logout request |

- request structure

| name | type | means |
|------|------|-------|

- return value

| name     | type         | means                            |
|----------|--------------|----------------------------------|
| response | JsonResponse | the result of the logout request |

- return dict structure

| name      | type | means                    |
|-----------|------|--------------------------|
| error_num | int  | the num of the error     |
| msg       | str  | the message of the error |

- error_num table

| values | means   |
|--------|---------|
|      0 | success |

## getTagList

- arguments

| name        | type   | means                  |
| ------      | ------ | ------                 |
| userid      | str    | user's identify symbol |
| currentPath | str    | user's tag path        |

- return value

| name   | type   | means                  |
| ------ | ------ | ------                 |
| result | dict   | a dict of return value |

- return dict structure

| name      | type   | means                |
| ------    | ------ | ------               |
| error_num | int    | error number         |
| msg       | str    | error message        |
| tagList   | list   | list of the son tags |

- error_num table

|  value | means             |
| ------ | ------            |
|      0 | succeed           |
|      1 | no son directory  |
|      2 | no such directory |


## getFileList
- auguments

| name        | type   | means                  |
| ------      | ------ | ------                 |
| userid      | str    | user's identify symbol |
| currentPath | str    | user's file path       |

- return value

| name   | type   | means                  |
| ------ | ------ | ------                 |
| result | dict   | a dict of return value |

- return dict structure

| name      | type   | means                               |
| ------    | ------ | ------                              |
| error_num | int    | error number                        |
| msg       | str    | error message                       |
| fileList  | list   | list of the files which has the tag |

- error_num table

|  value | means             |
| ------ | ------            |
|      0 | succeed           |
|      1 | no file           |
|      2 | no such directory |


## paperDown

- arguments

| name     | type   | means                     |
| ------   | ------ | ------                    |
| arxivID  | str    | the paper number in arxiv |
| paperDir | str    | download path             |

- return value

| name   | type   | means                     |
| ------ | ------ | ------                    |
| path   | str    | the path of this PDF file |

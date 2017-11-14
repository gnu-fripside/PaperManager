# Some Essential Functions of PaperManager
-------------
## getTagList
- auguments

| name | type | means |
| ------| ------ | ------ |
| userid | str | user's identify symbol |
| currentPath | str | user's tag path |

- return value

| name | type | means |
| ------| ------ | ------ |
| result | dict | a dict of return value |

- return dict structure

| name | type | means |
| ------| ------ | ------ |
| error_num | int | error number |
| msg | str | error message |
| tagList | list | list of the son tags |

- error_num table

| value | means |
| ------| ------ |
| 0 | succeed |
| 1 | no son directory |
| 2 | no such directory |


## getFileList
- auguments

| name | type | means |
| ------| ------ | ------ |
| userid | str | user's identify symbol |
| currentPath | str | user's file path |

- return value

| name | type | means |
| ------| ------ | ------ |
| result | dict | a dict of return value |

- return dict structure

| name | type | means |
| ------| ------ | ------ |
| error_num | int | error number |
| msg | str | error message |
| fileList | list | list of the files which has the tag |

- error_num table

| value | means |
| ------| ------ |
| 0 | succeed |
| 1 | no file |
| 2 | no such directory |

## add_book

- auguments

| name | type | means |
| ------| ------ | ------ |
| request | django request | add book request from frontend |

- return value

| name | type | means |
| ------| ------ | ------ |
| response | JsonResponse | the result of this add operation |

- return dict structure

| name | type | means |
| ------| ------ | ------ |
| error_num | int | error number |
| msg | str | error message |

- error_num table

| value | means |
| ------| ------ |
| 0 | succeed |
| 1 | operation failed caused by this exception |

## show_books

- auguments

| name | type | means |
| ------| ------ | ------ |
| request | django request | add book request from frontend |

- return value

| name | type | means |
| ------| ------ | ------ |
| response | JsonResponse | the result of this show book operation |

- return dict structure

| name | type | means |
| ------| ------ | ------ |
| error_num | int | error number |
| msg | str | error message |

- error_num table

| value | means |
| ------| ------ |
| 0 | succeed |
| 1 | operation failed caused by this exception |

## register

- auguments

| name | type | means |
| ------| ------ | ------ |
| request | django request | add book request from frontend |

- request structure

| name | type | means |
| ------| ------ | ------ |
| user_name | str | user name to be registered |
| user_password | str | user password |

- return value

| name | type | means |
| ------| ------ | ------ |
| response | JsonResponse | the result of this register operation |

- return dict structure

| name | type | means |
| ------| ------ | ------ |
| error_num | int | error number |
| msg | str | error message |

- error_num table

| value | means |
| ------| ------ |
| 0 | succeed |
| 1 | this user name has been registered |

## login

- auguments

| name | type | means |
| ------| ------ | ------ |
| request | django request | add book request from frontend |

- request structure

| name | type | means |
| ------| ------ | ------ |
| user_name | str | user name to be registered |
| user_password | str | user password |

- return value

| name | type | means |
| ------| ------ | ------ |
| response | JsonResponse | the result of this register operation |

- return dict structure

| name | type | means |
| ------| ------ | ------ |
| error_num | int | error number |
| msg | str | error message |
| cookie | str | when succeed, cookie exists |

- error_num table

| value | means |
| ------| ------ |
| 0 | succeed |
| 1 | wrong password |
| 2 | this user name does not exist |

## paperDown

- auguments

| name | type | means |
| ------| ------ | ------ |
| arxivID | str | the paper number in arxiv |
| paperDir | str | download path |

- return value

| name | type | means |
| ------| ------ | ------ |
| path | str | the path of this PDF file |

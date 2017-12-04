# All the models of PaperManager

## Users

- head_img

这是django中自带的model的fields，包括username，password，email等字段

- classification_tree_root

这是分类树的根节点，在用户注册后自动创建

- log

这是用户的“阅读时间线”

## ClassificationTree

- name 

这是分类树节点的名字

- father

这是分类树节点的父亲节点

## Paper

- title

这是论文的标题

- authors

这是论文的作者（们）

- publish_time

这是论文被发表的日期

- add_time

这是该论文被添加进来的时间

- source

这是论文被发表的期刊

- url

这是论文在网上的url

- hash_code

这是论文独有的哈希值

- classification_tree_node

这是论文所属的分类树的节点

- log 

这是该论文的log

- notes

这是论文的笔记

## Authors

- first_name

这是作者的名字

- last_name

这是作者的姓

- email

这是作者的邮箱

## Log

- log

这是论文的log

## Note

- paper_title

这是论文的标题

- paper_page

这是笔记所在论文的页码

- content

这是note本身


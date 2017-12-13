# PaperManager

---

## User Guide
- Install node.js and npm in your environment. If you are in mainland China, you need to install [cnpm](http://npm.taobao.org/) of Taobao.Inc.. If you use cnpm, the 'npm' in commands follow should be replaced by 'cnpm'.
- Goto the path of frontend (PaperManager/frontend/) and build the frontend.

<pre><code>
    npm install
    npm run build
</code></pre>

- for MySQL users, you should do this thing, set the MySQL default charset to UTF-8 as follows in my.cnf

<pre><code>
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mysql.conf.d/
[client]
default-character-set = utf8
[mysql]
default-character-set = utf8
[mysqld]
default-storage-engine=INNODB
character-set-server=utf8
collation-server=utf8_general_ci
</code></pre>

- Set the link in exportSrc function in showPdf.vue

- Goto previous path (PaperManager/) and start Django.

<pre><code>
    python3 manage.py runserver 8080
</code></pre>

---

## Develop Status

### DONE
- Register Module and Login Module
- Add Paper
- Paper Read Module
- Paper Info Module
- Tag Tree (show, click to son tags and backward enabled)
- Designing Universal Interface
- Add,Edit, and delete Notes 
- Export Module
- Share Module
- New UI(Element-UI supported)
- Optimizing Tag Tree display
- Writing Documentation
- Optimizing Web Page Design
- Final Test
### TODO
- A huge update with a lot of extensions of this website.
- Details can not be released right now.
- But I'm sure that new version will be extremely exciting. 


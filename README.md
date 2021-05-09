### We2RSS WeChat Official Account to RSS Service
---

#### Introduction

It’s a project to support transferring user’s subscription of **WeChat Official Account** to **RSS Service** for conveniently subscribing all information source the user is interested with only one RSS reading platform like **Rolly Rss Reader** in Android or **SSReader** in iOS.


#### How to start
1. Prepare a venv with your ide like PyCharm with Python3
2. Install all the requirement lib with the command below:  
    ```terminal
    pip3 install -r requirement.txt
    ```
3. Download chrome module into project directory with link below:

   https://pan.baidu.com/s/1hK2KbR2GBl_Qi-2ZzRaoGg 

   code: kpg8 

4. Create database and import structure and data

   Please create a MySQL database named “**wechat_official_account_passage_rss**”with “**utf8_general_ci**” encoding. Then create a MongoDB database named “**we2rss**” and create a collection named “**passage_collections**”. Meanwhile, you’re supposed to set your database configurations like host, port etc in `tools/db/db_core.py` and `tools/db/docs_db_core.py`.

5. login and get cookies for authorization
   
   Please make sure that you have done step3 then run `tools/core/login_wechat_official_account.py`
   
6. Have a try to do crawler by running `tools/core/request_history_article.py`, the crawler will get the WeChat Official Account and passage information into your database, please check your database after the crawler finished.
   

#### TODO

- [x] Assemble MySQL & MongoDB as storage for official account info and passage info
- [x] WeChat Crawler API
- [ ] Web frontend for user to operate
- [ ] Passage parsing and media link substitution with our own oss
- [ ] HTTP/ HTTPS Proxy for crawler


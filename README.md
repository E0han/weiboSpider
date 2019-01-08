### README - Weibo Spider
<hr>
Author: @0han

Email: 0han@pm.me

Chinese version document: [Not upload yet](ethyang.com)

<br>

##### What is this?
******
This script is used to download the specific target account's valuable posts (post that have more than 139 chars)on weibo.com, one of the biggest social media in the PRC, and the attached imgs. 
<br>

#####Effect:
******
> update later
<br>

##### Requirements
******
![](https://img.shields.io/pypi/pyversions/:3.svg) ![](https://img.shields.io/badge/Beautifulsoup4-Python%20--%20lib-green.svg)
![](https://img.shields.io/badge/Requests-Python%20--%20lib-blue.svg)

Use pip install both of them 
<br>

##### Preparation
******
- login to your account via m.weibo.cn on your laptop
- Searching your target, and get into his profile, record his "ID number" from the url like this:
> m.weibo.cn/profile/**189xxxxxxx**
- Your login info - mobile number and the password
<br>

##### Usage
******
- Open 'main.py'
- Replace the "ID number" with ur targets
- Replace the "Username" and "Passwd" strings with yours, remember **Im not going to record or push your personal information to any remote server** You can check this by go through the code.
- I suggest you check how many pages that ur target has via the url 
>weibo.cn/u/189xxxxxxx
 
 and replace the number of the For loop range. 
- [Option] you can change the sleep parameter by yourself, I set it as 8 seconds after each page be grabbed cuz I was tryin to make it works like a humanbeing, and I did not research the limitaion here, up to u
- run "python main.py", or whatever environment variable you use in the terminal.
- You will see there's a new file called text.txt and a folder called img which contains all the imgs if the post have one, named after the date of the post.

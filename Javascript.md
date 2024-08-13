|||
|-----|-------|
|Idiot Test| Open inspector and look for the javascript, if you have some understanding of how the code works then you know the password. If the x = cookies, it will send an alert that it is correct, the password is cookeis. |
|Disable Javascript| Open dev tools, go to settings. In Preference, under the Debugger, check mark 'Disable Javascript'. Click the arrow to go back, and click on the challenge again. Refreshing the site may not work. You may notice a link that will complete the challenge, upon doing so you may get a statement that is not the answer. Instead, right-click and open a new tab. You should complete the challenge.|
|Math time!|If you can do simple math it is easy, using PEMDAS and a calculator. Knowing that it ask for x.length = moo, we calculate that moo = 14. So entering a 14 random characters into the input box. We complete the challenge.|
|Var?|First step is to open the dev tools. You will come across another javascript function. This function check to see password you enter matches 'RawrRawr', the rest is throw you off. x == ""+RawrRawr+"" essentially concat empty string before and after so it's just literally moo which is the password. |
|Escape!|Like previous task, let's open dev tool and see what we can find. Upon inspection we find a javascript. Let see what it is, <code> moo = unescape('%69%6C%6F%76%65%6D%6F%6F'); </code> this is interesting, unsure what is unescape is I had to look it up. Which I found out that it replaces any escape sequence with the character that it represents. Removing the escape character and decoding the hex value in Cyberchef. I got <code>ilovemoo</code>, entering that in the challenge is completed.|
|go go away .js||
|JS Obfuscation. FTW!||

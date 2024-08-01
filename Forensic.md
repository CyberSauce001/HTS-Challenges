# First Time Go
You are tasked to recover a password. Go ahead download the attachment given and extract. Looking at the files, you can see the file format is .dd.
On Linux you want to down kpartx <code>sudo apt-get install kpartx</code>, then you will mount the image with this command <code>sudo kpartx -a -v file.dd</code>.<br><br>
However I am using Windows so I be using OSFMount for this challenge. Upon opening Stacy image. You notice that all the files within .Trash are empty. So it is possible we need
to recover them that Stacy deleted. I install a program call Recuva since it is free to restore delete files.<br><br>
After running the program and recovering, I look around, I see a rar file with the possible answer to the challenge. However I need a key to open it, looking more around. I listen the 
voicemail1.wav, this information tells me to use her phone number, which I found in a word doc. Copy and pasting her number I got the password, make sure to leave out the -, otherwise it won't work. 


# Cheater
You are tasked to find any manipulation on the image which will give you the password. I save the image to the desktop, and I did a bit search
on digital manipulation tools. This one caught my eye [Photo Forensics](https://29a.ch/photo-forensics/#forensic-magnifier). Playing around with it,
you will stumble upon Error Level Analysis. Modifying the scale value you will get the password.

# PapaSmurphey's Pizza
You are task to find the password with the flag format HTS{}, first download the file and extract it. After extracting and navigating into the folder. 
You are given a couple of files. Upon inspection, you should see something out of the ordinary. You can see that shh.jpg is over 10kMB that is highly suspicious. <br><br>
Using my favorite online tool [Aperisolve](aperisolve.fr/), I upload the image, then download foremost. Upon extraction I get another image with possible clue to something else.
However that can't be all the image is very large so something else must store in it. Throwing the image into a [Hex Editor](https://hexed.it/), we can see of course it is JPG image due to its header.<br><br>
Looking around the folder, I don't see much beside our next clue, 'siggies.txt', this particular file is mentioning about headers and trailer. So know JPG Header is start with  <code>FF D8 FF E0</code>, our ending should be 
<code>FF D9</code>, searching it we can see that there is more than one file in the image. Looking pass FF D9 we come across <code>5A 61 72</code>, doing '5A 51' yield no result, doing the next one '61 72' shows us that it
is a rar file. *Look at the siggies.txt to find the header*. 5A must be the padding. So how to extract?<br><br>
There are 2 ways you can use [Scalpel](https://github.com/sleuthkit/scalpel) or you can create a script to look for those header and trailer and then extract it from the image.

-wip

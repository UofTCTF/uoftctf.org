# Week 1

Here are some introductory resources:

[The difference between a Red Team and Blue Team.](https://youtu.be/jNY59pil8Tk)

[What is a CTF?](https://youtu.be/8ev9ZX9J45A)

This page is split into two sections - Beginner and non-beginner. If you are completely new to offensive security or computer science in general, it is highly encouraged that you to start in the beginner section as there are many new concepts, then move onto the proceeding section.

In some challenges, you may feel stuck or confused. Google is your best friend in these situations. Reading writeups (solutions to challenges) are also extremely helpful in learning. In many of the following exercises, writeups can be found publicly: Simply search up the challenge name and "writeup", and you will find one.

Note that you do not need to complete all exercises. Choose a category you like, and work from there! Every team member in a CTF has a role, and usually each will specialize in a specific category.

# Beginner

## Prepare your machine for CTFs!
1. Install a Virtual Machine (VM) on your computer - popular options are Oracle's Virtualbox or VMware. A virtual machine allows you to run a containerized operating system in your host environment!
2. Install linux on the VM - choose a distribution of your choice: [Ubuntu](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview), [Linux Mint](https://www.osboxes.org/linux-mint/), and [Manjaro](https://manjaro.org/download/) are popular options. There are many guides on how to download the distributions (usually in .iso form) and install them on the respective VMs. [Here's one for Virtualbox.](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview)
3. Play around with the VM! One of the most important things in CTFs is using the command line. The command line is the most direct interface a user has with the underlying operating system (computer). [Here's a guide on how to use the Linux command line.](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)

I encourage you to explore on your own and learn about some cool commands in the command line. How do you install external packages? Here's a challenge: Can you install and use `neofetch`?

## Learn some basic skills:

picoCTF has a great set of challenges in all categories of CTFs that you can try out. Register for an account on [picoCTF](https://picoctf.org), then try some out in picoGym. picoGym features almost all challenges from previous picoCTF competitions, so they are great practice! If you encounter any challenges from the `picoCTF 2022` section and are looking for writeups, here's a repo: https://github.com/Team-Carpe/picoCTF-2022

### picoCTF
[Exercises](https://play.picoctf.org/practice) - the "General Skills" section is great for building on foundational skills.

### Bandit
[Exercises](https://overthewire.org/wargames/bandit/) - Great site to start from!

### OSINT (Open source intelligence)
[Introduction](https://www.csnp.org/post/a-beginners-guide-to-osint)

### Web Exploitation 
[NATAS Exercises](https://overthewire.org/wargames/natas/) - Try to get up to level 5!

[TryHackMe Exercises](https://tryhackme.com/)

# Non-beginner

## Practice some skills!

The following is a list of some harder challenges. 

### Web exploitation
[NATAS](https://overthewire.org/wargames/natas/) - Can you get to level 10?

### Binary Exploitation (pwn)
[Introductory guide](https://www.hoppersroppers.org/roadmap/training/pwning.html)

[Repository with some basic challenges (the techniques are included so google them as you progress!)](https://github.com/tripoloski1337/learn-to-pwn)

### Reverse Engineering
There are tons of tools used to reverse engineer binaries and other executables. IDA, Ghidra, dnSpy, and many other decompilers are very popular in this field. 

[Here's a comprehensive guide with resources on reverse engineering.](https://bbinfosec.medium.com/reverse-engineering-resources-beginners-to-intermediate-guide-links-f64c207505ed)

### Forensics
Forensics are not always formally defined in CTFs as the forensic process/analysis is used in many difficult challenges. Try out some challenges on picoCTF! [Here are some written writeups on all of the picoCTF 2022 forensics challenges.](https://github.com/Team-Carpe/picoCTF-2022/tree/main/Forensics)

### Cryptography
[Here's a guide.](https://hashelse.medium.com/cryptography-for-absolute-beginners-3e274f9d6d66)
You can also practice cryptography on picoCTF. 

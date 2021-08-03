# Manga_Downloader



This only download from Mangafreak.net and stores in pdf form.<br>
Nothing very advanced, you will have to tinker in main file and change link and end chapter var each time, you wanna download some other thing.



To get the links.<br>Go to Mangafreak.net and search the manga you wanna download, after that copy the first download link. In my case, let's say<br>http://images.mangafreak.net:8080/downloads/Kanojo_Okarishimasu_1 and after remove the last number from the link.<br>So, http://images.mangafreak.net:8080/downloads/Kanojo_Okarishimasu_<br> This will be the link, you wanna give as input.



#Side Notes

The program might run into permission error, when it does, empty the pic folder and delete last chapter.
In the for loop, change the '0' to whatever number chapter is in directory.

Say, you ran into error on chapter 100, delete chapter 100 and put loop from 99.

# Purpose of development.

There are friends who have difficulty communicating at the school where I am serving in society. This school has services for these friends. This service utilizes images and TTS technology to make it easier for friends to talk. When you click on the image, it reads the description of the image as TTS. In this way, friends and teachers can talk.



We use these symbolic images at https://arasaac.org/. And for the development of services, images should be downloaded, selected, and updated. However, this site does not have Korean language support. It also recently deleted the ability to download multiple images at once. Therefore, it is a situation in which images have to be downloaded cumbersomely.



# Program function.

I tried to solve this problem. Using the API provided on the website and the Papago translation API provided by Naver.

First, the API of the image website was used. Returns the unique number of the recently uploaded image.

Second, it was checked which unique number was last downloaded to the computer.

Third, an English description of the downloaded image was requested to the Papago translation API. And I received a Korean explanation back.

Fourth, the unique number of the image and the Korean description were set as file names and automatically stored on the computer.



# The problem with the program.

The process was repeated continuously. The problem is that the number of free Papago APIs did not exceed 10,000 a day. And there is an image that is not necessary.

The unnecessary image was determined to be a part that required minimal manpower and solved by human selection. And Papago's free number problem solved the problem in a different direction by not having more than 10,000 images a day.



# The results of the program.

As a result, unnecessary time was reduced by minimizing the repetitive part. And I was able to increase the conversation time between students and teachers.

The service in which students and teachers communicate is currently being conducted privately.



Since then, several versions have been produced. The function of selecting a file name can be downloaded by selecting one of a unique number, a Korean description, a unique number, and a Korean description.

In addition, it added functions to automatically receive the latest files, receive multiple files with a specific number, and download only specific numbers.

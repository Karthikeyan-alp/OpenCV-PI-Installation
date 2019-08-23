# IMAGE PROCESSING-OPENCV



## GETTING STARTED
        
   <br>In this project we can see how to install an opencv in raspberry pi.A step by step approach is given to install the opencv and its dependent packages.</br>
   
   
## PREREQUISITES
 
   - Raspberry pi 3/3B+/4
   - Proper Internet connections
   - Raspbian stretch os
   
   
## INSTALLING

### Booting the OS

 The Initial step is to boot the raspbian os in the Memory card.</br>

Raspbian os link: http://downloads.raspberrypi.org/raspbian_full/images/raspbian_full-2019-04-09)/</br>
Etcher for writing the os : https://www.balena.io/etcher/ </br>
Sd card Formatter : https://www.sdcard.org/downloads/formatter/



### Expanding the File System

To Expand the File system(space) for Installing the opencv

     sudo raspi-config
     
   select the "Advance option" and click Enter.Click the "Expand file system" and press Enter.Then move the Pointer to finish by Right arrow keys and click Ok.It will reboot the os .
   
   If it not Rebooting.Type the command in Terminal.
   
      sudo reboot

   




**Installing opencv for Image processing**
 
 
 STEPS TO FOLLOW FOR INSTALLING OPENCV
 
<br> -Expanding the Filesystem.</br>
 -Installing the dependent package for Opencv.</br>
 -Download the Opencv and Opencv-contrib Zip file.</br>
 -Installing a Virtual Environment for Python.</br>
 -Installing the numpy.</br>
 -Installing the opencv.</br>
 -Change the Swap size.</br>
 -Testing the Opencv and its Dependent package.</br>

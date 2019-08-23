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


#Run all the below codes in Terminal



### Expanding the File System

To Expand the File system(space) for Installing the opencv

     sudo raspi-config
     
   select the "Advance option" and click Enter.Click the "Expand file system" and press Enter.Then move the Pointer to finish by Right arrow keys and click Ok.It will reboot the os .
   
   If it not Rebooting.Type the command in Terminal.
   
      sudo reboot
      
      
### UPGRADING OUR OS

   we can ugrade our os upto date by using the following commands.
   
   
      sudo apt-get update
      
      sudo apt-get upgrade


### INSTALLING DEPENDENT PACKAGES

   Running this commands in command line will Install the dependent package for Opencv.
   
   
      sudo apt-get install build-essential cmake pkg-config
      
      sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
      
      sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
      
      sudo apt-get install libxvidcore-dev libx264-dev
      
      sudo apt-get install libgtk2.0-dev libgtk-3-dev
      
      sudo apt-get install libatlas-base-dev gfortran
      
      sudo apt-get install python2.7-dev python3-dev
   
   
   It will take time according to the Internet speed.
   
   
   ### INSTALLING THE OPENCV AND ITS CONTRIB FILE
   
       cd
       
       wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
       
  It will Download the opencv Zip file from the github.
  
       wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
       
  It will Download the opencv Contrib Zip file from the github.
  
  The Next step is to unzip the files of opencv and opencv contrib
  
       unzip opencv.zip
       
       unzip opencv_contrib.zip
       
   ### INSTALLING PYTHON 3 
   
   Python2.7 is going to an end of its life so we are going to use an python3 .
   
   <br> Now we are installing a pip package
   
         wget https://bootstrap.pypa.io/get-pip.py
         
         sudo python3 get-pip.py
         
   ### INSTALLING VIRTUAL ENVIRONMENT
      
        sudo pip install virtualenv virtualenvwrapper
        
        sudo rm -rf ~/.cache/pip
        
   Now we want to make some changes to virtual environment source code.write the below code in terminal window.
         
        sudo nano ~/.profile
        
   The new terminal will open go to the last line
   
   
        # virtualenv and virtualenvwrapper
          export WORKON_HOME=$HOME/.virtualenvs
          export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
          source /usr/local/bin/virtualenvwrapper.sh
          
   Paste this code at last and press ctrl+X after that press Enter .
   
   Now you close the terminal and reopen a new terminal.
   
   
   ### CREATING A NEW PYTHON VIRTUAL ENVIRONMENT
   
   
           mkvirtualenv cv -p python3
     
   ### CHECKING THE VIRTUAL ENVIRONMENT
   
   
           cd
           
           source ~/.profile
           
           workon cv
           
   Now check whether you are in an virtual Enviroment.The cv is printed in from of your terminal window.
   
   ### INSTALLING A NUMPY 
   
   Now we are installing a numpy in our virtual Environment.check whether you are in a cv Environment.
   
   
           pip install numpy
           
   ### INSTALLING A OPENCV
   
   Now we are going to install a Opencv on pi.
   
   
            workon cv
            
            cd ~/opencv-3.3.0/
            
   Creating a new directory called build inside opencv -3.3.0 directory
   
             mkdir build
             
             cd build
             
             cmake -D CMAKE_BUILD_TYPE=RELEASE \
                   -D CMAKE_INSTALL_PREFIX=/usr/local \
                   -D INSTALL_PYTHON_EXAMPLES=ON \
                   -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
                   -D BUILD_EXAMPLES=ON ..
                   
   Now you can check Python3 interpreter showing cv path.That's all we came to the End.
   
   ### CONFIGURE THE SWAP SIZE
   
   In this step we are allocating our SD memory space as Ram.Run this code.
   
   




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

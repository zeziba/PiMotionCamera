<h3>PiMotionCamera</h3>
<p>Included in this package is a python 3 program that runs a Pi camera in conjunction with
a PIR motion sensor. The picture will be saved to a local NAS run by a samba server.
</p>
<p>In order to run the package there are a few setup steps needed
</p>
<p>If a NAS storage sever is desired I recommend the samaba server to store content on and retrive. 
To use the samaba server a Linux computer or Pi will have to be used to host it. As all the commands and
code is used to set-up and save to a samba server, it is require to have these tools installed
<a href="https://help.ubuntu.com/community/How%20to%20Create%20a%20Network%20Share%20Via%20Samba%20Via%20CLI%20(Command-line%20interface/Linux%20Terminal)%20-%20Uncomplicated,%20Simple%20and%20Brief%20Way!">Samaba</a>, follow this link to see how to install the samaba sever.</p>
<p>To run the package all you need is the included files unless you would like a NAS storage. To run the default package just follow these steps.</p>
<ul>
<li>Download the program as a zip</li>
<li>Extract to desired location</li>
<li>Open a terminal</li>
<li>Navigate to the PiMotionCamera folder</li>
<li>Navigate to the PiCameraServer</li>
<li>run sudo ./connect_server.sh</li>
<li>Navigate back to the PiMotionCamera folder by entering in cd ..</li>
<li>use python3 ./config_parser.py in the terminal</li>
<li>use python3 ./PiMotionCamera.py</li>
</ul>
<p>Following the above sets should allow the camera to start functioning and start taking pictures if motion is detected by the PIR sensor.</p>
<p>If the camera fails to take pictures ensure that everything is plugged in correctly and that the camera is enable in the configuration menu for the pi.</p>
<b>To connect to the Samba server you will need the following packages</b>
<ul>
<li>sambas</li>
<li>samba-common-bin</li>
<li>samba-client</li>
</ul>
<p>The above will allow you to work witht eh samba server</p>
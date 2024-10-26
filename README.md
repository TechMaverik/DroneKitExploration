# DroneKit Exploration
<b>Prerequisite: Python 3.9 Preferred (Above versions will crash drone kit)</b>
<h1>Install the following</h1>
<code>
pip3 install dronekit
</code>
<br>
<code>
pip3 install mavlink
</code>
<br>
<code>
pip3 install dronekit-sitl
</code>

<h1>How to run </h1>
Make serial connections to the flight controller from Raspberry pi and run the following sample commands.

<code>
python3 AutoPilot_Takeoff_Landing.py --connect /dev/ttyAMA0
</code>

Make sure to change the /dev/xxxx with your port

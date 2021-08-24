# VOSK-ROS
XXXXXX
### Umgebung
|Software|Version|
|--|--|
|Ubuntu|16.04 LTS|
|ROS|Kinetic Kame|
|Python|3.9|
|Catkin ws|0.7.29 with Python 3.9.4|
|VOSK|0.3.30|


### Hinweise | Anmerkungen
1. um Python 3.9 verwenden zu koennen musste "export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages" aus der .bashrc entfernt  oder per "unset PYTHONPATH" im Terminal ausgeblendet werden. Wenn Python 2.7 dist-packages geladen sind funktioniert ROSCORE und ROSPY nicht, da diese eine enum Alternative aus Python 3.9 verwenden. 
2. Wasser ist nass und die Kompatabilitaet dieses Packet ist naesser

### Probleme
1. Turtle "Gehe zu" Befehl kann in den Ecken haengen bleiben wenn nicht genug Platz fuer die Drehung gelassen wird  (z.B. X,Y:11,11 -> X,Y:11:0).
2. Turtle "Gehe zu" Befehl ignoriert negative Koordiaten. bzw. "parsed" das Minuszeichen nicht.
3. Die Turtle ist in der Lage zu Koordinaten zu gehen welche rationale Zahlen beinhalten, jedoch erlaubt der Befehl "Gehe zu" nur Natürliche Zahlen.


### Startanweisung
1. Starte ROSCORE
2. Starte "vosk_sr_ros.py"
3. Starte "mediator_turtle_sim_py"
4. (Optional) Starte "talker.py"
5. (soundplay sachen)
6. Starte turtlesim mit "rosrun turtlesim turtlesim_node"

### Ausführbare Befehle 
1. Rechts - Drehung nach rechts um 90 Grad
2. Links - Drehung nach links um 90 Grad
3. Vorwärts - Ein "Schritt" gerade aus
4. Rückwärts - Ein "Schritt" Rückwärts
5. Gehe zu *X* *Y* - Gehe zur Koordinate X, Y.  W = {X,Y ∈ ℕ | 1 ≤ X,Y ≤ 9}

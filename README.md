# VOSK-ROS
VOSK-ROS ist ein ROS Package, welches im Rahmen eines Praktikums im Wintersemester 2021 an der Technischen Hochschule Georg Agricola entwickelt wurde.
Die Aufgabe bestand darin, durch Spracherkennung, Sprache in Text umzunwandeln und, durch TextToSpeech, Text in Sprache umzuwandeln.
Zusaetzlich sollte ein Nutzer in der Laage sein Sprachbefehle an den Turtlesim weiterzugeben, um diesen Kontrollieren zu koennen.

### Inhaltsverzeichnis
<!--ts-->
   * [VOSK-ROS](https://github.com/C-Sahin/VOSK-ROS#VOSK-ROS)
   * [Inhaltsverzeichnis](https://github.com/C-Sahin/VOSK-ROS#Inhaltsverzeichnis)
   * [Umgebung](https://github.com/C-Sahin/VOSK-ROS#Umgebung)
   * [Hinweise | Anmerkungen](https://github.com/C-Sahin/VOSK-ROS#hinweise--anmerkungen)
   * [Probleme](https://github.com/C-Sahin/VOSK-ROS#Probleme)
   * [Startanweisung](https://github.com/C-Sahin/VOSK-ROS#Startanweisung)
   * [Ausführbare Befehle ](https://github.com/C-Sahin/VOSK-ROS#ausf%C3%BChrbare-befehle)
<!--te-->

### Umgebung
|Software|Version|
|--|--|
|Ubuntu|16.04 LTS|
|ROS|Kinetic Kame|
|Python|3.9|
|Catkin ws|0.7.29 with Python 3.9.4|
|VOSK|0.3.30|

|Verwendete ROS Packages|
|----|
|ros sound_play|


### Hinweise | Anmerkungen
1. um Python 3.9 verwenden zu koennen musste "export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages" aus der .bashrc entfernt  oder per "unset PYTHONPATH" im Terminal ausgeblendet werden. Wenn Python 2.7 dist-packages geladen sind funktioniert ROSCORE und ROSPY nicht, da diese eine enum Alternative aus Python 3.9 verwenden.

### Probleme
1. Turtle "Gehe zu" Befehl kann in den Ecken haengen bleiben wenn nicht genug Platz fuer die Drehung gelassen wird  (z.B. X,Y:11,11 -> X,Y:11:0).
2. Turtle "Gehe zu" Befehl ignoriert negative Koordiaten. bzw. "parsed" das Minuszeichen nicht.
3. Die Turtle ist in der Lage zu Koordinaten zu gehen welche rationale Zahlen beinhalten, jedoch erlaubt der Befehl "Gehe zu" nur Natürliche Zahlen.


### Startanweisung
1. Starte ROSCORE mit "```roscore```"
2. Starte die Vosk-Spracherkennung mit "```rosrun vosk_ros vosk_sr_ros.py```"
3. Starte den Vermittler zwischen der Spracherkennung und Turtlesim mit "```rosrun vosk_ros mediator_turtle_sim.py```"
4. (Optional) Starte den Vermittler zwischen der Spracherkennung und der Sprachausgabe (echo) mit "```rosrun vosk_ros mediator_tts.py```"
5. (Optional) Starte die Sprachausgabe (echo) mit sound_play mit "```rosrun sound_play soundplay_node.py```"
6. Starte die Turtlesim mit "```rosrun turtlesim turtlesim_node```"

![RQT_Graph](/img/rosgraph.png)


### Ausführbare Befehle 
1. Rechts - Drehung nach rechts um 90 Grad
2. Links - Drehung nach links um 90 Grad
3. Vorwärts - Ein "Schritt" gerade aus
4. Rückwärts - Ein "Schritt" Rückwärts
5. Gehe zu *X* *Y* - Gehe zur Koordinate X, Y.  W = {X,Y ∈ ℕ | 1 ≤ X,Y ≤ 9}

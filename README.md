# mesh
#MESH

# Titel unserer Solution
Go New

# Slogan unserer Solution
-reinvent mobilty-

# das ist unsere Solution
Wir möchten ländliche ÖPNV revolutionieren, indem wir einen Algorithmus entwerfen, welcher mittels einer App dem User die Möglichkeit gibt, seine gewünschte Route im voraus einzugeben. Ein von uns beauftragtes Fahrzeug bringt dann den User von Punkt A nach Punkt B. Dies wird kombiniert, dass viele User ihre Routen eingeben und der Algorithmus die optimale Route berechnet und so möglichst viele User, welche in etwa dasselbe Ziel haben und in der Nähe voneinander starten, aufsammelt und die Ziele in einem Maß abfährt, sodass jeder sein Ziel vor der von ihm angegebenen Zeit erreicht. 
Unser Ziel ist es damit die momentanen Anbindungen der ländlichen Regionen auszutauschen und eine wesentlich effektivere Alternative zu entwickeln, da es heutzutage oft passiert, dass einige sehr große Busse mit wenig Personen rumfahren und auch die Zeiten zu wünschen übrig lassen. Mit unserer Methode werden die Busse direkt nach den Bedürfnissen der Menschen zu Verfügung gestellt. Mithilfe der Userdaten kann man direkt auch die Größe des benötigten Busses bestimmen, sodass es nicht zu dem Fall kommt, dass ein großer Bus mit keiner Person auf der Straße zu sehen ist. 
In der Zukunft kann man das ganze auch perfekt fahrerlos gestalten, indem die Busse einfach von dem Algorithmus aus losgeschickt werden. Während wir am Anfang primär auf kleine, mit fossilien Brennstoffen basierenden Busse bauen müssen, ist es natürlich unser Ziel diese möglichst schnell durch alternative Energien zu ersetzten wie z.B. Elektrobusse zu ersetzen.

In unserem Programm sind wir nun so weit gekommen, dass der Algorithmus aus mehreren Eingaben herausfindet, wie er die Personen aufsammelt und halbwegs an passenden Zielorten absetzt. Implementiert werden müsste noch eine bessere Kalkulierung des Zieles, eine gute Eingabe der Koordinaten per String, sodass nicht die ganze Zeit die Koordinaten eingeben werden müssen. Des Weiteren muss natürlich das Frontend  der eigentlichen App entworfen werden. Beim ersten Start der App muss das Land, das Bundesland und ein Landkreis ausgewählt werden, mit welchem dann das Programm die Kalkulationen besser und schneller vornehmen kann. Momentan befindet sich diese Eingabe des Standortes noch per String in Zeile 13.

Beispiel:
Nehmen wir mal an, dass 5 Leute die App testweise nutzen: Personen 1-3 leben (recht nah voneinander) in  Dorf1 und Personen 4+5 leben in Dorf2 und Dorf3. Alle haben unterschiedliche Ziele in derselben Stadt ausgewählt. Nun fährt unser Bus an eine Haltestelle in Dorf 1 und sammelt dort Person 1-3 auf. Nun fährt der Bus nach Dorf2 und Dorf3 und sammelt dort die anderen Menschen auf. Er setzt seine Fahrt zum Zielort fort und setzt alle Menschen am Zielort ab (Falls jetzt das Ziel von 2 Personen in Laufdistanz voneinander ist, wird (wenn möglich) die Mitte von diesen beiden Orten gewählt und beide Personen können dort aussteigen, so wird Zeit gespart.



# Teammitglieder 
Felix Marwede,
Marius Beck,
David Honekamp,
Marius Wergen,
Niels Krüger,

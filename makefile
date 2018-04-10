
grafica2.pdf : Graph2.py dataEc2.txt
	python Graph2.py

grafica1.pdf : warmingGraph.py dataEc.txt
	python warmingGraph.py

dataEc2.txt : Ejerc2
	./Ejerc2 > dataEc2.txt


dataEc.txt : DataEc
	./DataEc > dataEc.txt

DataEc2 : 
	c++ ejercicio2.cpp -o Ejerc2

DataEc : 
	c++ warmingup.cpp -o DataEc
	

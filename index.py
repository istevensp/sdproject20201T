#!/usr/bin/env python
import cgi,cgitb
import MySQLdb as mariadb

print "Content-Type: text/html;charset=utf-8"
print "\n\n"
print "<html>"
print "<head>"
#print '<link href= "control.css" rel="stylesheet" type="text/css">'
print "<title>"
print "Grafica temperatura"
print "</title>"

print "<script type=\"text/javascript\"src=\"https://www.google.com/jsapi\"></script>"
print "<script type=\"text/javascript\">"
print "google.load('visualization', '1', {packages:['corechart']});"
print "google.setOnLoadCallback(drawChart);"

db = mariadb.connect("mdbp-1.cun4wfkxlev9.us-west-2.rds.amazonaws.com","admin","stevendayana","proyectotest1")
curs = db.cursor()
curs.execute("SELECT * FROM temps order By fecha DESC limit 0,150")

print "	     function drawChart() {"
print "	       var data = google.visualization.arrayToDataTable(["
print "		 ['Fecha', 'Humedad', 'Temperatura']"
for data in curs.fetchall():
	print ",['"+str(data[1])+"',"+str(data[3])+","+str(data[2])+"]"
print		 "]);"
db.close()

print "		   var options = {"
print "		     title: 'Temperatura'	 };"
print "		   var chart = new google.visualization.LineChart(document.getElementById('chart_div'));"
print "		   chart.draw(data, options);	   }"
print "	       </script>"

print "</head>"
print "<body>"
print "<h1><center>Grafica de temperatura y humedad</center></h1>"
print "<center>"
print '<div id="chart_div" style="width: 1200px; height: 500px;"></div>'
print "<h2></h2>"
print '<a href="index.py"><img src="reload.png" width="100" height="100" alt="Achatada" border="0"></a>'
print "</center>"
#print '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">'
#print '<meta http-equiv="refresh" content="5;URL=http://50.112.74.58//index.py">'
print "</body>"
print "</html>"


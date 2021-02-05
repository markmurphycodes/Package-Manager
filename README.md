

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Package Manager</h3>

  <p align="center">
 An application of graph algorithms to the traveling salesman problem.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#algorithm-overview">Algorithm Overview</a>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About the project
# Stated Problem:

The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day; each package has specific criteria and delivery requirements.

Your task is to determine the best algorithm, write code, and present a solution where all 40 packages, listed in the attached “WGUPS Package File,” will be delivered on time with the least number of miles added to the combined mileage total of all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map” and distances to each location are given in the attached “WGUPS Distance Table.”

While you work on this assessment, take into consideration the specific delivery time expected for each package and the possibility that the delivery requirements—including the expected delivery time—can be changed by management at any time and at any point along the chosen route. In addition, you should keep in mind that the supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and what time the delivery occurred.

The intent is to use this solution (program) for this specific location and to use the same program in many cities in each state where WGU has a presence. As such, you will need to include detailed comments, following the industry-standard Python style guide, to make your code easy to read and to justify the decisions you made while writing your program.

# Assumptions:

* Each truck can carry a maximum of 16 packages.
* Trucks travel at an average speed of 18 miles per hour.
* Trucks have a “infinite amount of gas” with no need to stop.
* Each driver stays with the same truck as long as that truck is in service.
* Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. The day ends when all 40 packages have been delivered.
* Delivery time is instantaneous, i.e., no time passes while at a delivery (that time is factored into the average speed of the trucks).
* There is up to one special note for each package.
* The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
*  The package ID is unique; there are no collisions.
*  No further assumptions exist or are allowed.


This program is designed using an object-oriented design. All data transfer and processing is done via object reference. Python is inherently modular (Python 2020) and the problem is, at its core, about the interaction between physical objects which made modular OOP a great fit for the problem.




### Built With


* [Python](docs.python.org/3/)



## Algorithm Overview:
The problem is to be solved as following:
* 1.	Packages are loaded onto the trucks according to the specifications defined in the package file.
* 2.	Packages sharing addresses with these existing packages are loaded onto the corresponding trucks.
* 3.	Using Christofides algorithm, a eulerian circuit is found in the remaining packages’ nodes.
* 4.	For all trucks, a eulerian circuit is found for the nodes to be traveled by each.

* O(n^m) where n is the number of trucks and m is the number of packages <br />
```
  for truck in trucks:
	  truck.packages = hard-coded
	  truck.packages += packages sharing address information with existing, hard-coded packages
```

* O(n) <br />
```
  for package in remaining packages: 
  	remainingNodes.append(package.address)
```


* O(n^2 * log(n)) <br />
```
  bestPath = remainingNodes.tsp   # get a eulerian circuit from all remaining nodes
```


* O(n^2 * n(log(n))) due to the Christofides algorithm being called <br />
```
  for truck in trucks:
  	while there is space in the truck:
  		add as many stops from the remaining nodes as possible
  		calculate eulerian circuit for all priority nodes and the rest as separate circuits
  determine which node in the non-priority nodes is closest to the last node of the priority ones.
  append the non-priority nodes to the priority nodes, starting with the closest determined in the next step
  ```

As there are multiple possible eulerian circuits possible in a complete graph, several iterations of package assignment may be necessary to find an optimal path which accommodates all delivery times. The best path is tracked and returned.




<!-- CONTACT -->
## Contact

Mark Murphy - mark@markmurphy.codes

Project Link: [github](https://github.com/markmurphycodes/Package-Manager)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements


* [“Christofides Algorithm.” Wikipedia](en.wikipedia.org/wiki/Christofides_algorithm)
* [Lysecky, Roman, and Frank Vahid. Data Structures and Algorithms II. 2018](learn.zybooks.com/zybook/WGUC950AY20182019)
* [Multiple Traveling Salesman Problem (MTSP) | NEOS](neos-guide.org/content/multiple-traveling-salesman-problem-mtsp)
* [Retsediv/ChristofidesAlgorithm](github.com/Retsediv/ChristofidesAlgorithm)





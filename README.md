# A-Star Route Planner

An Artificial Intelligence project that uses the A* Search Algorithm to find optimal routes between stations based on different optimization criteria.

---

# Project Overview

The system simulates a transportation network consisting of stations connected by roads and transportation methods.

A traveler starts with an initial amount of money and energy and attempts to reach the destination station using the best possible route.

The system can optimize the route according to:

* Minimum Cost
* Minimum Energy Consumption
* Minimum Travel Time

---

# State Representation

Each state is represented by a Node class.

## Node Attributes

* Park_id: Current station identifier
* Energy: Remaining energy
* Time: Total elapsed time
* Money: Remaining money
* Transport_type: Current transportation method
* Parent: Parent state

---

# Transportation Methods

The system supports:

* Walking
* Bus
* Taxi

Each transportation method affects:

* Money
* Energy
* Time

---

# Main Functions

## printDetails()

Displays:

* Station name
* Remaining energy
* Remaining money
* Consumed time
* Available transportation methods

## isFinal()

Checks whether the destination station has been reached.

## canMove()

Verifies that:

* Enough money is available.
* Energy remains positive.
* The move is valid.

## move()

Generates the next state.

## nextNode()

Generates all valid successor states.

---

# A* Search Algorithms

## FirstAstar()

Finds the route with the minimum monetary cost.

## SecondAstar()

Finds the route with the minimum energy consumption.

## ThirdAstar()

Finds the route with the minimum travel time.

Each algorithm:

* Uses a priority queue.
* Maintains visited states.
* Expands successor nodes.
* Applies heuristic evaluation.
* Returns the optimal route.

---

# Route Reconstruction

## getRoute()

Recursively reconstructs the final path using parent references.

## play()

Executes the selected optimization mode.

---

# Data Structures

## Stations

Stations are stored in an array.

## Roads

Roads are represented using a Map structure.

## Search States

States are stored as Node objects.

## Priority Queue

Used by the A* algorithm to expand nodes according to heuristic values.

---

# Artificial Intelligence Concepts

* State Space Search
* A* Search Algorithm
* Heuristic Functions
* Path Planning
* Priority Queues
* Graph Traversal

---

# Features

* Route optimization by cost.
* Route optimization by energy.
* Route optimization by time.
* Multiple transportation methods.
* Dynamic state generation.
* Path reconstruction.
* Heuristic search.

---

# Technologies Used

* Java
* Object-Oriented Programming (OOP)
* A* Search Algorithm
* Graph Search
* Priority Queue
* Artificial Intelligence

---

# Sample Output

Add screenshots of the generated routes and results inside the screenshots folder.

## Route Planning Example

![Result](screenshots/result.png)

---

# Academic Project

This project was developed as part of Artificial Intelligence coursework and demonstrates the application of heuristic search algorithms for transportation route planning.


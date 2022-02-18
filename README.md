Airport Challenge
=================

```
        ______
        _\____\___
=  = ==(____MA____)
          \_____\___________________,-~~~~~~~`-.._
          /     o o o o o o o o o o o o o o o o  |\_
          `~-.__       __..----..__                  )
                `---~~\___________/------------`````
                =  ===(_________)

```

## Motivation
This project was originally completed using [Ruby](https://github.com/marcusventin/airport_challenge). I have repeated it in order to gain experience using Python.  

The project enables a user to simulate basic airport / airplane interactions. It is intended to satisfy the following user stories:

> As an air traffic controller,  
> So I can get passengers to a destination,  
> I want to instruct a plane to land at an airport.

> As an air traffic controller,  
> So I can get passengers on the way to their destination,  
> I want to instruct a plane to take off from an airport and confirm that it is no longer in the airport.

> As an air traffic controller,  
> To ensure safety,  
> I want to prevent landing when the airport is full.

> As the system designer,  
> So that the software can be used for many different airports,  
> I would like a default airport capacity that can be overridden as appropriate.

> As an air traffic controller,  
> To ensure safety,  
> I want to prevent takeoff when weather is stormy.

> As an air traffic controller,  
> To ensure safety,  
> I want to prevent landing when weather is stormy.

## Features
Airports can instruct airborne planes to land and grounded planes to take off. A random stormy weather variable keeps budding air traffic controllers on their toes though!

## How to Use
#### Set-Up
1. Fork this repository and clone it to your machine.
2. Check there are no problems with the code by running `pipenv shell` in your terminal to set up a virtual environment, followed by `pytest` - all being well, the tests will pass.
3. Run `python3` to initialise your REPL.
4. Enter `from airport import Airport` to load the airport class.
5. Enter `from plane import Plane` to load the airport class.
6. Enter `from weather import Weather` to load the weather class.
7. Play to your heart's content using the commands listed below.

#### Airport Methods
`NAME = Airport(optional maximum capacity)` - creates a new Airport object and set a custom maximum capacity - the default is currently set to 8.  
`.land(plane)` - lands an object of the Plane class and stores it in the airport's hangar.  
`.launch(plane)` - launches an object of the Plane class and removes it from the airport's hangar.  

#### Plane Methods
`NAME = Plane()` - creates a new Plane object.  
`.land(airport)` - adds the plane to an airport's hangar, and calls the `.ground()` function to update its status.  
`.take_off(airport)` - removes the plane from an airport's hangar, and calls the `.fly()` function to update its status.  
`.ground()` - updates the plane's status to show it is on the ground.
`.fly()` - updates the plane's status to show it is in the air.

#### Weather Methods
`.storm_check()` - returns True if there's a storm brewing!

## Sample REPL Interaction
```
>>> from airport import Airport
>>> from plane import Plane
>>> from weather import Weather
>>> heathrow = Airport(2)
>>> gatwick = Airport(1)
>>> andsimple = Plane()
>>> ex = Plane()
>>> asday = Plane()
>>> gatwick.land(andsimple)
>>> heathrow.land(andsimple)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/marcusventin/Projects/python_extensions/python-airport-challenge/airport.py", line 14, in land
    raise Exception("Your plane is in another airport!")
Exception: Your plane is in another airport!
>>> gatwick.land(ex)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/marcusventin/Projects/python_extensions/python-airport-challenge/airport.py", line 18, in land
    raise Exception("There's no space in this hangar!")
Exception: There's no space in this hangar!
>>> heathrow.launch(andsimple)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/marcusventin/Projects/python_extensions/python-airport-challenge/airport.py", line 24, in launch
    raise Exception("Your plane is in another airport!")
Exception: Your plane is in another airport!
>>> andsimple.airborne
False
>>> gatwick.launch(andsimple)
>>> andsimple.airborne
True
```

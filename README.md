## eats_and_does

### Part 1

* Create a new directory in your `nb-<first_name>-<last_name>` repo.

* In a file named `eats.py`, define three classes: `Bear`, `Turtle`, and 
`Sasquatch`. For each, define a method: `eats()`. This should return "berries" for the `Bear`, "insects and small fish" for the `Turtle`, and "hazelnuts" for the `Sasquatch`. Create one object from each and print what it eats.

* In a file named `does.py`, define three classes: `HeadLight`, `DriveTrain`, and `SoundSystem`. For each, define a method: `does()`. This returns "illuminates" for the `HeadLight`, "propels" for the `DriveTrain`, and "rocks" for the `SoundSystem`. Then define the class `Car` that has one instance (object) of each of these classes.

  Define a `does()` method for the Car that prints what its component objects do.


### Part 2

* Add data attributes to `Bear`, `Turtle`, and `Sasquatch` that can be used to order instances of each relative to one another: first names for Bears, K-12 reading level for turtles, area code for Sasquatch.

  Overload the <, <=, >, and >= operators for these three classes to reflect this ordering.

  Put together some print statments that show this ordering in effect.

* Create a class `Electronic` from which `Headlight` and `SoundSystem` are inhereted. 

  Add an instance varaiable (aka data attribute) for each object that will show if it is turned on or off. 

  Write an instance method that will turn an object of class `Electronic` on and off.

  Add a class variable to `Electronic` that tracks how many instances of the class have been created over the duration of the program and a class method that returns or prints this value.

  (see slide deck `Week04_part3` for examples of a class method and class-level data attribute) 

  Create three cars with a `Headlight`, `DriveTrain`, and `SoundSystem` and print the attribute in `Electronic` that has counted how many total `Electronic`s have been created.

### Submission

* When you're done, push your code up to bitbucket and let me know in lab.
* For credit, we'll do a brief demo and you'll get feedback in person.

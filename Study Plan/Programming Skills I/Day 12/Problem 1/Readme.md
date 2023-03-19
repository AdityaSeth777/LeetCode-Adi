Problem -> <https://leetcode.com/problems/design-parking-system/description/?envType=study-plan&id=programming-skills-i>


The ParkingSystem class has an __init__ method that initializes the number of slots for each type of parking space. The slots are stored in a list, where the index represents the car type (1 for big, 2 for medium, and 3 for small), and the value represents the number of available slots for that type of space.

The addCar method checks whether there is an available slot for the specified car type. If there is, it decrements the number of available slots for that type of space and returns True. Otherwise, it returns False.

Note that this implementation assumes that the input values for big, medium, and small are non-negative integers. If the input values can be negative or non-integer, you may need to add input validation to the __init__ method.

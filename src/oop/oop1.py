# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: #base class
    
    pass

#-------- GroundVehicles
class GroundVehicle(Vehicle): #inherits from base class
    pass


class Car(GroundVehicle): #inherits from subclass GroundVehicle
    pass

class Motorcycle(GroundVehicle): #inherits from subclass GroundVehicle
    pass
#---------- GroundVehicles

#-------- FlightVehicles
class FlightVehicle(Vehicle): #inherits from base class
    pass


class Starship(FlightVehicle): #inherits from subclass GroundVehicle
    pass

class Airplane(FlightVehicle): #inherits from subclass GroundVehicle
    pass
#---------- FlightVehicles


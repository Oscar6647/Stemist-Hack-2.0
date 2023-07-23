from enum import Enum

chosenSubject = ""

class Subject(Enum):
    Math = "The class study plan is about math."
    Spanish = "The class study plan is about spanish."
    Biology = "The class study plan is about biology."
    Physics = "The class study plan is about physics."

class BiologySubtopics (Enum): 
    HumanBody = "With a focus on the human body"
    FoodChain = "With a focus on the food chain"
    Environment = "With a focus on the environment"

class MathSubtopics (Enum):
    AdditionSubtraction = "With a focus on addition and substraction"
    MultiplicationDivision = "With a focus on multiplication and division"
    Fractions = "With a focus on fractions"

class SpanishSubtopics (Enum):
    Spelling = "With a focus on spelling"
    Reading = "With a focus on reading"
    Writing = "With a focus on writing"

class PhysicsSubtopics (Enum):
    Movement = "With a focus on movement"
    ForceGravity = "With a focus on force and gravity"
    Matter = "With a focus on matter"

class Time(Enum):
    LessThan1Hour = "The class lasts less than 1 hour long"
    MoreThan1Hour = "The class lasts more than 1 hour long"

class Age(Enum):
    GreaterThan9 = "The class study plan is aimed for kids older than 9 years old. Please provide some recommendations for the teacher to improve their class study plan:"
    LowerThan9 = "The class study plan is aimed for kids younger than 9 years old. Please provide some recommendations for the teacher to improve their class study plan:"

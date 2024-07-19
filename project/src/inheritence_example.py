class Mother:
    def speak(self):
        print("speaks like mother")
class Father:
    def speak(self):
        print("speaks like father")

class Child(Father, Mother):
    pass

child = Child()

child.speak()


# df.withColumn("sum", F.sum("column").partitionBy(Window.partitionBy("column2")))
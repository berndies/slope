from bernd_plot import Plot

MAX_ENTRIES = 4

# Lists:
xList = []
yList = []
slopeList = []


class Slope:

    def __init__(self, max):
        self.max = max

    def enter_values(self):
        for i in range(0, self.max):
            my_str = f"Enter x{i}: "
            value = int(input(my_str))
            xList.append(value)

            my_str = f"Enter y{i}: "
            value = int(input(my_str))
            yList.append(value)

    def calc_slope(self, first, second):
        xdiff = xList[second] - xList[first]
        # print("xdiff", xdiff)
        ydiff = yList[second] - yList[first]
        # print("ydiff", ydiff)
        if xdiff != 0:
            slo = ydiff/xdiff
            # print("Slope", slo)
            slopeList.append(slo)
        else:
            print("Cannot divide by zero !!! - x values are the same")

    def check_slope_is_the_same(self):
        tmp_slope = slopeList[0]
        for i in range(1, len(slopeList)):
            if (slopeList[i] != tmp_slope):
                print("Slopes are different!")
                return False
        print("Slopes are the same:", slopeList[0])
        return True

    def print_lists(self):
        print("X:    ", xList)
        print("Y:    ", yList)
        print("Slope:", slopeList)


mySlope = Slope(MAX_ENTRIES)

mySlope.enter_values()

for i in range(1, MAX_ENTRIES):
    # print("Calling calc with ", i+1, "and", i)
    mySlope.calc_slope(i, i-1)

mySlope.print_lists()
mySlope.check_slope_is_the_same()

# Plot the graph
myPlot = Plot("Slope")
myPlot.set_axis_labels("Apples", "Bananas")
myPlot.display_plot(xList, yList, mySlope.max)

import matplotlib.pyplot as plt


class Bernd:
    # Just a test to try inheritance
    def __init__(self, name):
        self.author = name


class Plot(Bernd):

    def __init__(self, title, style='seaborn'):
        # Test how to call super class init
        super().__init__("Bernd Seidinger")

        self.title = title
        self.style = style
        self.xlabel = "x-axis"
        self.ylabel = "y-axis"

    def set_axis_labels(self, xstr, ystr):
        self.xlabel = xstr
        self.ylabel = ystr

    def display_plot(self, x, y, max):
        plt.style.use(self.style)
        fig, ax = plt.subplots()

        # display the dots
        for i in range(0, max):
            ax.scatter(x[i], y[i], s=200, c='blue')

        # draw the line
        ax.plot(x, y, linewidth=3)

        ax.set_title(self.title, fontsize=24)
        ax.set_xlabel(self.xlabel, fontsize=14)
        ax.set_ylabel(self.ylabel, fontsize=14)
        ax.tick_params(axis='both', labelsize=14)
        # display the plot
        plt.show()

    def test_plot(self):
        xList = [1, 2, 3, 4, 5, 6, 7]
        yList = [1, 4, 9, 16, 25, 36, 49]
        max = len(xList)
        self.display_plot(xList, yList, max)


# testPlot = Plot("Test Plot")
# print("Written by", testPlot.author)
# testPlot.test_plot()

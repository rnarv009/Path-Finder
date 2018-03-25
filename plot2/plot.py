import matplotlib.pyplot as plt

# line 1 points
x1 = [14, 48, 100, 150, 300, 400]
y1 = [3459, 6828.91, 9008.74, 11490, 17833, 38465.79 ]
# plotting the line 1 points
plt.plot(x1, y1, label="NN")

# line 2 points
x2 = [14, 48, 100, 150, 300, 400]
y2 = [3153, 6049.91, 8262.2643, 10496.973, 21090.9274, 30192.317]
# plotting the line 2 points
plt.plot(x2, y2, label="GA")

x3 = [14, 48, 100, 150, 300, 400]
y3 = [4634,9874.95,14476.23,17636,29396.862,32861]
plt.plot(x3, y3, label="ACO")

# naming the x axis
plt.xlabel('No. of nodes')
# naming the y axis
plt.ylabel('Total cost')
# giving a title to my graph
plt.title('Comparison of NN vs GA vs ACO for solving TSP')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
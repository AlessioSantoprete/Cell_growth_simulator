import matplotlib.pyplot as plt

# GROWTH RATE HIGHER
N = 1 #number of cells
r = 0.2 #  growth rate
d = 0.1 # death rate
t = 0 # time

# Lists: cells_number_growth and time_values
cells_number_growth = [1] # initial cells
time_values = [0] # Initial time value

for t in range(0, 50):
    N = N + (r * N - d * N) #Change in cell number
    cells_number_growth.append(N) # adds cells to the list
    time_values.append(time_values[-1] + 1) # store time step in the list

print(cells_number_growth)
print(time_values)

# DEATH RATE HIGHER
N = 100 #number of cells
r = 0.1 #  growth rate
d = 0.2 # death rate

cell_numbers_decay = [100] # initial cells

for t in range(0, 50):
    N = N + (r * N - d * N) #Change in cell number
    cell_numbers_decay.append(N) # adds cells to the list

print(cell_numbers_decay)
print(time_values)


# Plot Graph Growth
plt.figure()
plt.plot(time_values, cells_number_growth)
plt.title("Cell Growth Over Time")

# Plot Graph Decay
plt.figure()
plt.plot(time_values, cell_numbers_decay)
plt.title("Cell Decay Over Time")

#Display the graph
plt.show()
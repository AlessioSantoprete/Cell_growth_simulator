import streamlit as st
import matplotlib.pyplot as plt

# GROWTH RATE HIGHER
N = st.number_input("Please enter the initial number of cells: ", min_value=1, step=1) #number of cells
r = st.number_input("Please enter the growth rate: ", min_value=0.0, step=0.01) #  growth rate
d = st.number_input("Please enter the death rate: ", min_value=0.0, step=0.01) # death rate
steps = st.number_input("Please enter the number of steps: ", min_value=1, step=1)
K = st.number_input("Please enter the carryign capacity: ", min_value=1, step=1) #Carrying capacity --> limit
t = 0 # time

# Lists: cells_number_growth and time_values
cells_number = [N] # initial cells
time_values = [0] # Initial time value
initial_N = N
if initial_N > K:
    st.warning("Initial population exceeds carrying capacity. Population will decrease toward equilibrium.")


for t in range(int(steps)):
    N = N + (r * N * (1- N / K) - d * N) #Change in cell number
    cells_number.append(N) # adds cells to the list
    time_values.append(time_values[-1] + 1) # store time step in the list

st.write("Final number of cells: ", round(N))

# INTERPRETATION
if r > d:
    st.write("Population is growing over time")
elif r < d:
    st.write("Population is declining over time")
else:
    st.write("Population remains stable")


# Plot Graph
plt.figure()
plt.plot(time_values, cells_number, label="Cell Population")
plt.title("Cell Growth Over Time")
plt.xlabel("Time")
plt.ylabel("Number of Cells")
plt.grid() # adds the grid to the graph
plt.axhline(y=K, linestyle="--", label="Carrying Capacity (K)")
plt.axhline(y=N, linestyle=":", label="Equilibrium")
plt.legend()

#Display the graph
st.pyplot(plt)
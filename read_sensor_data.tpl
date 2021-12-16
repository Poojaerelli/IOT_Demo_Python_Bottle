%import time
%import pandas as pd
%import matplotlib.pyplot as plt
%from matplotlib.animation import FuncAnimation
<%
    def animate(i):
        data = pd.read_csv('acc_readings.csv')
        x_values = data['time']
        y1_values = data['X-co']
        y2_values = data['Y-co']
        y3_values = data['Z-co']
        plt.cla()
        plt.plot(x_values, y1_values, linewidth=1, color='orange', label='X co-ord')
        plt.plot(x_values, y2_values, linewidth=1, color='blue', label='Y co-ord')
        plt.plot(x_values, y3_values, linewidth=1, color='brown', label='Z co-ord')
        plt.xlabel('Time')
        plt.ylabel('Acceleration')
        plt.title('Accelerator sensor readings')
        plt.legend()
        plt.gcf().autofmt_xdate()
        plt.tight_layout()
        time.sleep(1)
    end
%>
%ani = FuncAnimation(plt.gcf(), animate, 1000)
%plt.tight_layout()
%plt.show()

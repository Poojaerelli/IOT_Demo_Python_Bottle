from bottle import run, Bottle, template

app = Bottle()


@app.route('/')
def func():
    #yield 'Hello World!'
    yield 'Displaying Accelerator readings graph in X, Y and Z co-ordinates:'

    return template('read_sensor_data.tpl')


run(app=app, host='localhost', port=8080, debug=True, reloader=True)



















'''def animate(i):
        data = pd.read_csv('acc_readings.csv')
        x_values = data['time']
        y1_values = data['X-co']
        y2_values = data['Y-co']
        y3_values = data['Z-co']
        plt.cla()
        plt.plot(x_values, y1_values, linewidth=0.7)
        plt.plot(x_values, y2_values, linewidth=0.7)
        plt.plot(x_values, y3_values, linewidth=0.7)
        plt.xlabel('time')
        plt.ylabel('Acceleration')
        plt.title('Accelerator sensor readings')
        # plt.gcf().autofmt_xdate()
        plt.tight_layout()

    ani = FuncAnimation(plt.gcf(), animate, 1000)
    plt.tight_layout()
    # plt.show()'''

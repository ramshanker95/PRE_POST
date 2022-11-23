import rplidar
import time
from math import floor

def process_data(data):
    print(len(data))


scan_data = [0] * 360
PORT_NAME = 'COM3'
def run(): 
    '''Main function'''
    lidar = rplidar.RPLidar(PORT_NAME)
    old_t = None
    data = []
    try:
        print('Press Ctrl+C to stop')
        lidar.motor_speed = rplidar.MAX_MOTOR_PWM
        for scan in lidar.iter_scans(min_len=100, max_buf_meas=False):
            # print(scan)
            for (_, angle, distance) in scan:
                scan_data[min([359, floor(angle)])] = distance
                print("angle :",floor(angle) ,"-->",floor(distance))
                # print("distance",floor(distance))
            process_data(scan_data)
            now = time.time()
            if old_t is None:
                old_t = now
                continue
            delta = now - old_t
            print('%.2f Hz, %.2f RPM' % (1/delta, 60/delta))
            data.append(delta)
            old_t = now
    except KeyboardInterrupt:
        print('Stoping. Computing mean...')
        lidar.stop()
        lidar.disconnect()
        delta = sum(data)/len(data)
        print('Mean: %.2f Hz, %.2f RPM' % (1/delta, 60/delta))

if __name__ == "__main__":
    run()
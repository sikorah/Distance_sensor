from machine import time_pulse_us
import importlib
import time
import gpio_init as gpio

disp = importlib.import_module('7_seg_disp')

def main():
    echo_pin, trig_pin = gpio.init_sensor_gpio()
    start_stop_pin= gpio.init_start_stop_gpio()
    segments = gpio.init_7_segment_gpio()

    while True:
        if start_stop_pin.value() == 1:
            trig_pin.value(0)
            time.sleep_us(2)
            trig_pin.value(1)
            time.sleep_us(10)
            trig_pin.value(0)

            pulse_duration = time_pulse_us(echo_pin, 1, 30000)
            if pulse_duration <= 0:
                distance_cm = 0
            else:
                distance_cm = int(pulse_duration / 58)

            disp.display_number(segments, distance_cm)
            
            time.sleep_ms(60) 

        elif start_stop_pin.value() == 0:
            for seg in segments:
                for pin in seg:
                    pin.value(0)
            time.sleep_ms(100) 
            
        else:
            time.sleep_ms(50)

if __name__ == '__main__':
    main()
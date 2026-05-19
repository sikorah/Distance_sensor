import machine
import SegDisp as disp
import time
import gpio_init as gpio

def main():
    echo_pin, trig_pin = gpio.init_sensor_gpio() # Inicjalizacja GPIO dla czujnika ultradźwiękowego
    start_stop_pin= gpio.init_start_stop_gpio() # Inicjalizacja GPIO dla przycisku start/stop
    segments = gpio.init_7_segment_gpio() # Inicjalizacja GPIO dla wyświetlaczy 7-segmentowych

    while True:
        if start_stop_pin.value() == 1:
            disp.show_startup_message(segments)  # Wyświetl komunikat startowy
            time.sleep_ms(2000)  # Czekaj 2 sekundy aby zobaczyć komunikat
            trig_pin.value(1)
            time.sleep_us(15) # Sygnał wyzwalający mierzenie -- 15us (min.10us)
            trig_pin.value(0)

            pulse_duration = machine.time_pulse_us(echo_pin, 1, 30000) # Pomiar długości impulsu ECHO (okres proporcjonalny do zmierzonej odległości) z timeoutem 30ms
            if pulse_duration <= 0:
                distance_cm = 0
            else:
                distance_cm = (pulse_duration / 58.7545) # Przeliczanie czasu trwania impulsu na odległość w cm (przy prędkości dźwięku ~343 m/s)

            disp.display_distance(segments, distance_cm)
            
            time.sleep_ms(60) 

        elif start_stop_pin.value() == 0:
            for seg in segments:
                for pin in seg:
                    pin.value(0)
            disp.show_stop_message(segments)
            time.sleep_ms(100) 
            
        else:
            time.sleep_ms(50)

if __name__ == '__main__':
    main()
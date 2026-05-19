from machine import Pin

def init_sensor_gpio():
    ECHO_PIN = Pin(27, Pin.IN)
    TRIG_PIN = Pin(28, Pin.OUT)
    TRIG_PIN.value(0)
    return ECHO_PIN, TRIG_PIN

def init_start_stop_gpio():
    START_STOP_PIN = Pin(15, Pin.IN, Pin.PULL_DOWN)
    return START_STOP_PIN

def init_7_segment_gpio():
    SEGMENT_PINS_SEG1 = [Pin(i, Pin.OUT) for i in [0, 1, 2, 3, 4, 5, 6]]
    SEGMENT_PINS_SEG2 = [Pin(i, Pin.OUT) for i in [8, 9, 10, 11, 12, 13, 14]]
    SEGMENT_PINS_SEG3 = [Pin(i, Pin.OUT) for i in [17,18,19,20,21,22,26]]
    for pin in SEGMENT_PINS_SEG1:
        pin.value(0)
    for pin in SEGMENT_PINS_SEG2:
        pin.value(0)
    for pin in SEGMENT_PINS_SEG3:
        pin.value(0)
    return SEGMENT_PINS_SEG1, SEGMENT_PINS_SEG2, SEGMENT_PINS_SEG3
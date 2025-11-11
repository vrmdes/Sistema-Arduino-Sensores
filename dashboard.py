# Leitura simples da porta serial (ajuste a porta conforme seu sistema)
try:
    import serial, time
    ser = serial.Serial('COM3', 9600, timeout=1)
    import time
    time.sleep(2)
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print('>>', line)
except Exception as e:
    print('Exemplo para leitura serial. Se não usar porta, execute e verá mensagem:', e)

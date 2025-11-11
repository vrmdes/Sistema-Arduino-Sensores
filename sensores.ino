// Exemplo mínimo sem dependências externas
void setup(){
  Serial.begin(9600);
}
void loop(){
  Serial.println("Temperatura: 25.0 C | Umidade: 60%");
  delay(2000);
}

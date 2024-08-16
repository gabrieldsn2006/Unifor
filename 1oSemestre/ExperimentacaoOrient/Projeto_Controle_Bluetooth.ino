#include <SoftwareSerial.h>
int dirB = 7;
int dirA = 6;
int esqA = 5;
int esqB = 4;
int bluetoothTx = 9;  // Pino TX do módulo Bluetooth conectado ao RX do Arduino
int bluetoothRx = 8;  // Pino RX do módulo Bluetooth conectado ao TX do Arduino
// Inicialização do objeto para comunicação Bluetooth
SoftwareSerial bluetooth(bluetoothRx, bluetoothTx);
void Parar() {
  digitalWrite(dirA, HIGH);
  digitalWrite(dirB, HIGH);
  digitalWrite(esqA, HIGH);
  digitalWrite(esqB, HIGH);
}
void Seguir_em_Frente() {
  digitalWrite(dirB, HIGH);
  digitalWrite(dirA, LOW);
  //digitalWrite(dirB, LOW);
  //digitalWrite(dirA, HIGH);
  digitalWrite(esqB, HIGH);
  digitalWrite(esqA, LOW);
  //digitalWrite(esqB, LOW);
  //digitalWrite(esqA, HIGH);
}
void Re() {
  digitalWrite(dirB, LOW);
  digitalWrite(dirA, HIGH);
  //digitalWrite(dirB, HIGH);
  //digitalWrite(dirA, LOW);
  digitalWrite(esqB, LOW);
  digitalWrite(esqA, HIGH);
  //digitalWrite(esqB, HIGH);
  //digitalWrite(esqA, LOW);
}
void Virar_para_Esquerda() {
  digitalWrite(dirB, HIGH);
  digitalWrite(dirA, LOW);
  //digitalWrite(dirB, LOW);
  //digitalWrite(dirA, HIGH);
  digitalWrite(esqB, LOW);
  digitalWrite(esqA, HIGH);
  //digitalWrite(esqB, HIGH);
  //digitalWrite(esqA, LOW);
}
void Virar_para_Direita() {
  digitalWrite(dirB, LOW);
  digitalWrite(dirA, HIGH);
  //digitalWrite(dirB, HIGH);
  //digitalWrite(dirA, LOW);
  digitalWrite(esqB, HIGH);
  digitalWrite(esqA, LOW);
  //digitalWrite(esqB, LOW);
  //digitalWrite(esqA, HIGH);
}
void setup() {
  Serial.begin(9600);
  bluetooth.begin(9600);
  for (int x = 4; x < 8; x++) pinMode(x, OUTPUT);
}
void loop() {
  if(bluetooth.available() > 0) {
    char direcao = bluetooth.read();
    if (direcao == 'u') Seguir_em_Frente(); // informação recebida: 'u' do botão UP no app inventor
    else if (direcao == 'd') Re(); // informação recebida: 'd' do botão DOWN no app inventor
    else if (direcao == 'l') Virar_para_Esquerda(); // informação recebida: 'l' do botão LEFT no app inventor
    else if (direcao == 'r') Virarr_para_Direita(); // informação recebida: 'R' do botão RIGHT no app inventor
    else Parar(); // informação de parada recebida caso nenhum botão seja pressionado
  }
}
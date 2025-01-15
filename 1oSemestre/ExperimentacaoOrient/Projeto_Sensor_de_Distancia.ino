#include <Servo.h>
Servo myServo;
int t1 = 330; // tempo para o servo mover 90 graus 
int t2 = 250; // tempo para o carrinho virar em 90 graus
int dirB = 7;
int dirA = 6;
int esqA = 5;
int esqB = 4;
// função usada para leitura do sensor de distância
long Read_UD(int triggerPin, int echoPin) {
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  return pulseIn(echoPin, HIGH);
}
// as funções para movimentação do carrinho são semelhantes as utilizadas no código anterior
void Parar() {
  digitalWrite(dirA, HIGH);
  digitalWrite(dirB, HIGH);
  digitalWrite(esqA, HIGH);
  digitalWrite(esqB, HIGH);
}
void Seguir_em_Frente() {
  //digitalWrite(dirB, HIGH);
  //digitalWrite(dirA, LOW);
  digitalWrite(dirB, LOW);
  digitalWrite(dirA, HIGH);
  digitalWrite(esqB, HIGH);
  digitalWrite(esqA, LOW);
  //digitalWrite(esqB, LOW);
  //digitalWrite(esqA, HIGH);
}
void Virar_para_Esquerda() {
  digitalWrite(dirB, LOW);
  digitalWrite(dirA, HIGH);
  //digitalWrite(dirB, HIGH);
  //digitalWrite(dirA, LOW);
  digitalWrite(esqB, HIGH);
  digitalWrite(esqA, LOW);
  //digitalWrite(esqB, LOW);
  //digitalWrite(esqA, HIGH);
  delay(t2);
  Seguir_em_Frente();
}
void Virar_para_Direita() {
  digitalWrite(dirB, HIGH);
  digitalWrite(dirA, LOW);
  //digitalWrite(dirB, LOW);
  //digitalWrite(dirA, HIGH);
  digitalWrite(esqB, LOW);
  digitalWrite(esqA, HIGH);
  //digitalWrite(esqB, HIGH);
  //digitalWrite(esqA, LOW);
  delay(t2);
  Seguir_em_Frente();
}
void setup() {
  Serial.begin(9600);
  myServo.attach(11, 500, 2500);
  myServo.write(90);
  for (int x = 4; x < 8; x++) pinMode(x, OUTPUT);
  Seguir_em_Frente();
}
void loop() {
  long Distancia_Atual = Read_UD(A0, A1);
  if (Distancia_Atual < 700) {
    Parar();
    myServo.write(180);
    delay(t1);
    long Dist_Esquerda = Read_UD(A0, A1);
    myServo.write(0);
    delay(2*t1);
    long Dist_Direita = Read_UD(A0, A1);
    myServo.write(90);
    Dist_Esquerda >= Dist_Direita ? Virar_para_Esquerda() : Virar_para_Direita();
  }
  delay(20);
}
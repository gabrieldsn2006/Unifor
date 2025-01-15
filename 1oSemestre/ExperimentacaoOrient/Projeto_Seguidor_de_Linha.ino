int velA = 150; // velocidade usada para rodas no sentido LOW
int velB = 255 - velA; // velocidade usada para rodas no sentido HIGH
int dirB = 7; // porta usada para informar o sentido em que a roda direita irá girar
int dirA = 6; // porta pwm usada para controlar a velocidade da roda direita
int esqA = 5; // porta pwm usada para controlar a velocidade da roda esquerda
int esqB = 4; // porta usada para informar o sentido em que a roda esquerda irá girar
int sensorDir = 12; // porta do sensor infravermelho direito
int sensorEsq = 3; // porta do sensor infravermelho esquerdo
int Leitura_do_Sensor = 1; // leitura do sensor sobre uma superfície escura
// funções para movimentação do carrinho 
void Parar() {
  digitalWrite(dirA, HIGH);
  digitalWrite(dirB, HIGH);
  digitalWrite(esqA, HIGH);
  digitalWrite(esqB, HIGH);
}
void Seguir_em_Frente() {
  digitalWrite(dirB, LOW);
  analogWrite(dirA, velA);
  //digitalWrite(dirB, HIGH);
  //analogWrite(dirA, velB);
  digitalWrite(esqB, LOW);
  analogWrite(esqA, velA);
  //digitalWrite(esqB, HIGH);
  //analogWrite(esqA, velB);
}
void Seguir_para_Esquerda() {
  digitalWrite(dirB, LOW);
  analogWrite(dirA, velA);
  //digitalWrite(dirB, HIGH);
  //analogWrite(dirA, velB);
  digitalWrite(esqA, HIGH);
  digitalWrite(esqB, HIGH);
}
void Seguir_para_Direita() {
  digitalWrite(dirB, HIGH);
  digitalWrite(dirA, HIGH);
  digitalWrite(esqB, LOW);
  analogWrite(esqA, velA);
  //analogWrite(esqA, velB);
  //digitalWrite(esqB, HIGH);
}
void setup(){
  for (int x = 4; x < 8; x++) pinMode(x, OUTPUT);
  pinMode(sensorDir, INPUT);
  pinMode(sensorEsq, INPUT);
}
void loop(){
  if (digitalRead(sensorEsq) == Leitura_do_Sensor && digitalRead(sensorDir) == !Leitura_do_Sensor) { // caso a leitura dos sensores seja 1 e !1 (1 e 0)
    Seguir_para_Esquerda();
  } else if (digitalRead(sensorEsq) == !Leitura_do_Sensor && digitalRead(sensorDir) == Leitura_do_Sensor) { // caso a leitura dos sensores seja !1 e 1 (0 e 1)
    Seguir_para_Direita();
  } else if (digitalRead(sensorEsq) == !Leitura_do_Sensor && digitalRead(sensorDir) == !Leitura_do_Sensor) { // caso a leitura dos sensores seja !1 e !1 (0 e 0)
    Seguir_em_Frente();
  } else { // caso a leitura dos sensores seja 1 e 1
    Parar();
  }
}

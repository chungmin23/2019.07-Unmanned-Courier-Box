#include "HX711.h"              // 로드셀 함수
#include <SPI.h>               // RFID 통신 함수
#include <MFRC522.h>            // RFID 메인 함수
#define SS_PIN         8          // sck 9 MISO 10 MOSI 11
#define RST_PIN         7
#define NR_OF_READERS   1         

byte ssPins[] = {SS_PIN};         // RFID 변수 선언
int buzzer1 = 23;               // 부저1
int buzzer2 = 22;               // 부저2

unsigned long standTime1 = 0; 
unsigned long standTime2 = 0; 
unsigned long curTime;


MFRC522 mfrc522[NR_OF_READERS];      // RFID 함수 선언

HX711 scale(A1, A0);            // DT A1, SCK A0 2층 1번
HX711 scale2(A3, A2);            // DT A3, SCK A2 1층 2번

int hol_flag = 0;


void setup()
{ 
   Serial.begin(9600);            // 시리얼 통신
   SPI.begin();               // SPI 통신

   pinMode(3,OUTPUT);            // 1번째 LED 초록
   pinMode(4,OUTPUT);            // 1번째 LED 빨강
   pinMode(5,OUTPUT);            // 2번째 LED 초록
   pinMode(6,OUTPUT);            // 2번째 LED 빨강
   pinMode(29,OUTPUT);            // 솔레노이드1 
   pinMode(30,OUTPUT);            // 솔레노이드2
   pinMode(24,INPUT_PULLUP);      // 홀센서1
   pinMode(25,INPUT_PULLUP);      // 홀센서2

   scale.set_scale(2280.f);      // 첫번 째 로드셀 값
   scale.tare();                
   scale2.set_scale(2280.f);      // 두번 째 로드셀 값 
   scale2.tare();
  
   for(uint8_t reader = 0; reader < NR_OF_READERS; reader++)
   {
      mfrc522[reader].PCD_Init(ssPins[reader], RST_PIN);   // Init each MFRC522 card
      mfrc522[reader].PCD_Init(SS_PIN, RST_PIN);            // Init each MFRC522 card
      mfrc522[reader].PCD_DumpVersionToSerial();
   }
} 

void loop()
{
   
   for(uint8_t reader = 0; reader < NR_OF_READERS; reader++)
   {
      if(mfrc522[reader].PICC_IsNewCardPresent() && mfrc522[reader].PICC_ReadCardSerial())
      {
         dump_byte_array(mfrc522[reader].uid.uidByte, mfrc522[reader].uid.size);
         Serial.println();
         mfrc522[reader].PICC_HaltA();
         mfrc522[reader].PCD_StopCrypto1();
      }
   }
  

   if(scale.get_units(10) < -20)     // 1번 째 로드셀 무게 감지 되었을 때 1번 째 LED 빨강 시리얼 '0' 보냄
   {
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);      
    //  Serial.println(0);
   }
   else                      // 1번 째 로드셀 무게 감지 안 되었을 때 1번 째 LED 초록 시리얼 '1' 보냄
   {
      digitalWrite(5,LOW);
      digitalWrite(6,HIGH);
     // Serial.println(1);
   }

   if(scale2.get_units(10) < -20)   // 2번 째 로드셀 무게 감지 되었을 때 2 번 째 LED 빨강 시리얼 '2' 보냄
   {
      digitalWrite(3,HIGH);
      digitalWrite(4,LOW);   
   //   Serial.println(2);
   }
   else                     // 2번 째 로드셀 무게 감지 안 되었을 때 2 번 째 LED 초록 시리얼 '3' 보냄
   {
      digitalWrite(3,LOW);
      digitalWrite(4,HIGH);
   //   Serial.println(3);
   }

   curTime = millis();
   if (hol_flag == 1)
   {
       
       if(digitalRead(24) == HIGH)          // 홀센서가  반응하면( 문이 닫히면)
       {  
              
          digitalWrite(29,LOW);           // 솔레노이드가 작동한다(문고리가 닫힘)
          noTone(buzzer1);   
          hol_flag = 0;
          Serial.println("10");             // 시리얼 '10'을 보낸다
       }
          
       if(digitalRead(24) == LOW)
       {   
                    
           if(curTime - standTime1 >= 2000)
           {             
          //    tone(buzzer1,500);           // 시리얼 '10'을 보낸다
              
           }
       }       

    }
    else if (hol_flag == 2)
    {
         
         if(digitalRead(25) == HIGH)          // 홀센서가  반응하면( 문이 닫히면)
         {
            digitalWrite(30,LOW);           // 솔레노이드가 작동한다(문고리가 닫힘)
            noTone(buzzer2);
            hol_flag = 0;
            Serial.println("11");             // 시리얼 '10'을 보낸다
         }
                  
         if (digitalRead(25) == LOW)
         {
            if(curTime - standTime2 >= 2000)
           {       
           //   tone(buzzer2,500);           // 시리얼 '10'을 보낸다
              
           }
          
         }

          

    }
   if(Serial.available())         
   {
      char READ = Serial.read();             // 1번째 보관함
      if(READ == '5')                      // 시리얼 '5'가 들어오면 
      {
         digitalWrite(29,HIGH);             // 솔레노이드 작동한다(문고리가 열럼)
         hol_flag = 1;
         standTime1 = millis();                 
      }
      
      if(READ == '6')                      // 시리얼 '5'가 들어오면 
      {
         digitalWrite(30,HIGH);             // 솔레노이드 작동한다(문고리가 열럼)
         hol_flag = 2;  
         standTime2 = millis();             
      }

   }
 

}

void dump_byte_array(byte *buffer, byte bufferSize)
{
   tone(buzzer1,523,100); 
   for(byte i = 0; i < bufferSize; i++)
   {
      Serial.print(buffer[i],HEX);
   }
   
   Serial.println(",rfid");
}

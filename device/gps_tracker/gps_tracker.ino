#include <SoftwareSerial.h>
#include "SIM900.h"
#include "inetGSM.h"
//#include "sms.h"

#define DEBUG_ON

//To change pins for Software Serial, use the two lines in GSM.cpp.

//Simple sketch to start a connection as client.

InetGSM inet;
//SMSGSM sms;

char msg      [50];
char inSerial [50];
int  i = 0;
boolean started = false;
int tcp_port = 10000;
char server_addr [50] = "199.175.49.10";

void setup() {
     // serial connection to the PC
     Serial.begin(115200);
     Serial.println("GSM Shield testing.");
     // start configuration of shield with baudrate.
     // for http uses it is recommended to use 4800 or slower.
     if (gsm.begin(4800)) {
          Serial.println("\nstatus=READY");
          started=true;
     } else Serial.println("\nstatus=IDLE");

     if(started) {
          //GPRS attach, put in order APN, username and password.
          //If no needed auth let them blank.
          if (inet.attachGPRS("internet", "", "")) {
               Serial.println("status=ATTACHED");
          }
          else { 
               Serial.println("status=ERROR");
          }
          delay(1000);

          //Read IP address.
          char* resp = "OK";
          Serial.println(gsm.SendATCmdWaitResp("AT+CIFSR", 5000, 100, resp, 1));
          Serial.println(resp);
          Serial.println("here");
          gsm.SendATCmdWaitResp("AT+CIPSTART=\"TCP\",\"199.175.49.10\",10000", 5000, 100, resp, 1);
          Serial.println("here1");
          while (1) {
              gsm.SendATCmdWaitResp("AT+CIPSEND=3", 5000, 100, resp, 1);
              gsm.SimpleWrite("hi\n");
              Serial.println("sending data...");
              delay(5000);
          }

          //gsm.SimpleWriteln("AT+CIFSR");
          //delay(5000);
          //Read until serial buffer is empty.
          //gsm.WhileSimpleRead();

          //Connect to the server over a raw TCP connection
          //gsm.SimpleWrite("AT+CIPSTART=\"TCP\",\"");
          //gsm.SimpleWrite(server_addr);
          //gsm.SimpleWrite("\",");
          //gsm.SimpleWriteln(tcp_port);
          /*while (!inet.connectTCP(server_addr, tcp_port)) {
               Serial.println("failed to connect to " + String(server_addr) + " on port " + tcp_port);
               Serial.println("Trying again in 10 seconds");
               delay(10000);
          }*/
          //Serial.println("connected to " + String(server_addr) + " on port " + tcp_port);

     }
};

void loop() {
     //Read for new byte on serial hardware,
     //and write them on NewSoftSerial.
     //serialhwread();
     //Read for new byte on NewSoftSerial.
     //serialswread();
     //delay(1000);
     //x = random(100);
     //inet.sendRawTCPData("hello12345");
     //gsm.SimpleWriteln("Hello");
     //Serial.println("Hello");
};

void serialhwread() {
     i=0;
     if (Serial.available() > 0) {
          while (Serial.available() > 0) {
               inSerial[i]=(Serial.read());
               delay(10);
               i++;
          }
          inSerial[i]='\0';
          if(!strcmp(inSerial,"/END")) {
               Serial.println("_");
               inSerial[0]=0x1a;
               inSerial[1]='\0';
               gsm.SimpleWriteln(inSerial);
          }
          //Send a saved AT command using serial port.
          if(!strcmp(inSerial,"TEST")) {
               Serial.println("SIGNAL QUALITY");
               gsm.SimpleWriteln("AT+CSQ");
          }
          //Read last message saved.
          if(!strcmp(inSerial,"MSG")) {
               Serial.println(msg);
          } else {
               Serial.println(inSerial);
               gsm.SimpleWriteln(inSerial);
          }
          inSerial[0]='\0';
     }
}

void serialswread() {
     gsm.SimpleRead();
}
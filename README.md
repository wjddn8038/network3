# network_202144025
### 라즈베리파이 초기 설정
---
sudo apt update

sudo apt upgrade

### 한글깨짐

sudo apt-get install fonts-unfonts-core -y

sudo apt-get install ibus ibus-hangul -y

sudo reboot

## 구동 완료

InfluxDB 설치
---
    InfluxDB download key using wget
    wget -q https://repos.influxdata.com/influxdata-archive_compat.key
    echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee     
    /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
    echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list

Packages are up to date && install Influxdb
   
    sudo apt-get update && sudo apt-get install influxdb -y


InfluxDB as a background service on startup

        sudo service influxdb start
        InfluxDB is status (service)
        sudo service influxdb status

InfluxDB 데이터베이스 만들기
---
$ influx

>create database <데이터베이스이름>
>
        확인 : show databases 
        Grafana Installation
        
1. Repository의 GPG key를 더하기
   
        wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
   
2. Repository를 더하기
   
        echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

6. 프로그램 설치
   
        sudo apt update
        
        sudo apt install grafana

7. 프로그램 실행
   
        sudo service grafana-server start
        
        influxdb import with python
    
        pip install influxdb

## 구동 완료

Camera && TelegramBot
---
          pip install python-telegram-bot --upgrade
          
          git clone https://github.com/python-telegram-bot/python-telegram-bot --recurisive

  
PI 카메라 연결
---
        Legacy Camera disable
        libcamera-hello -t 0
      
Python Lib 설치

       pip install picamera2
  
Error

        libEGL warning : DRI2: failed to authenticate
        Made X/EGL preview window
        [1773] INFO Camera camera_manager.cpp:297 libcamera v0.0.5+83-bde9b04f
        ERROR: *** no cameras available ***

## 구동 완료

참고

 https://github.com/raspberrypi/picamera2/blob/main/examples/capture_png.py

## timerbot을 이용해 텔레그램에 사진 보내기

### 아직 구동 못함

## API

공공데이터의 미세먼지 검색을 통해 대기오염정보 API 활용 신청
미리보기를 통해 문서중 일부분을 미리볼수가 있음
파이썬은 DECODING 코드를 사용함
코드 dustAPI.py 를 입력 후 실행시 아까 미리봤던 화면이 출력됨
실행시 오류가 났을때 프로그램이 안깔렸을 수가 있으니 bs4와 requests, 또는 urllib를 다운

        pip install bs4
        pip install requests   or  pip install urllib

---

# 기말고사 프로젝트 아이디어(미정)
내가 생각한 주제
1. 날씨측정 라즈베리 파이
2. 음악재생 스트리밍 라즈베리 파이

# 기말고사 프로젝트 아이디어 (확정)
## 카메라를 이용한 라즈베리 파이 프로젝트(한용준) <----- 아이디어

카메라를 이용한 주제를 통한 아이디어(본인 아이디어)
1. 보안 cctv (카메라를 설치하고, 그 카메라에 사람이나 움직이는 것이 인식되면 자동으로 동영상이 녹화되는 시스템), 움직이는 것을 인식해서 학습하는 머신러닝 구축
2. 강의 스트리밍 (강의 시간에 맞춰 강의 시작시간에 녹화가 시작하게하고 수업이 끝날때 녹화가 끝난후 그 데이터를 사용자에게 보내는 시스템), 일정 시간이 될때마다 카메라를 끄고 켤수있는 파이썬 코드 구축
3. QR 코드 스캐너 ( QR 코드를 읽어들여 정보를 사용자에게 전달하는 시스템), qr코드를 학습해 읽을수 있는 머신러닝 구축
4. 글자 인식 번역카메라 ( 글자를 카메라로 인식하여 사용자에게 출력하고, 필요하다면 번역을 할수 있는 시스템), 글자를 인식해 읽어들이고 번역할수있는 모델을 구축
5. 얼굴 인식 카메라 ( 사람의 얼굴을 인식해서 그 사용자가 지금 어떤 기분인지 사용자에게 알려주는 시스템), 사람의 다양한 표정들을 학습하여 인식시 그때의 기분이 나오는 머신러닝 구축
6. 실시간 라이브 cctv ( 사용자가 cctv를 통해 화면을 보고싶을때 웹 또는 모바일로 카메라에 접속해 실시간으로 화면을 볼수있는 시스템), 웹 또는 모바일 앱을 통해 카메라로 원격 접속할수있는 웹이나 앱 구축
7. 스캐너 카메라 ( 사진이나, 책을 스캔하여 스캔본을 만들어주는 시스템), 사진, 책을 인식하여 스캔할수있는 모델 구축

## 팀원들 끼리 추론한 아이디어 및 기능
CCTV (카메라, 적외선 센서)
1. 보안용 CCTV: 사람의 움직임 감지시 동영상 녹화 또는 실시간 확인 시스템
1-1. 기능 추가 고려사항: 실내용 CCTV가 아닌 다방면의 방향성 모색

2. 글자 인식 카메라 (카메라)
2-2 글자 번역 제공 카메라
2-3 사진 및 책, 문서 스캐너

3. 시각장애인 보조 지팡이 (GPS, RFID, UWB모듈 중 한가지 사용)
   횡단보도, 차도 등에 도착시 시각장애인에게 도로의 정보를 제공
3-1. 기능 추가 고려사항: 도착시 시각장애인 신호 알림 받을 수 있는 방향 모색

4.차량 전화번호 태그기기 (NFC, RFID 등 태그관련 모듈 사용)
  핸드폰으로 태그시 시스템을 통한 차주인에 대한 정보제공(안심번호, 문자전송, 로그기록) 

참고 자료
https://return-value.tistory.com/106 (cctv 모션감지)
https://m.blog.naver.com/icbanq/221645472769 /   https://m.blog.naver.com/roboholic84/221382397929 (인체감지센서)



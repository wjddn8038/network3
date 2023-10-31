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

1. 날씨측정 라즈베리 파이
2. 음악재생 스트리밍 라즈베리 파이



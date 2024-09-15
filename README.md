# 유통기한 임박알림

#### 기획
편의점, 슈퍼마켓과같은 매장은 매일 유통기한을 확인하는 일이 필수적이며, 특히 유제품은 신속한 관리가 필요한다.
이러한 반복적인 작업을 줄여 효율적인 운영을 위해 서비스를 기획

#### 요구사항
- 유제품에 한해 알림
- 유통기한 1일전 유제품은 처리해야함
- 매일 오후 6시 빼야하는 유제품의 알람을 보낸다

#### 기술스택
- Web: Vue.js
- Server: Flask
- Dev: Aws[ lambda, CloudWatch Events, S3, SNS, RDS ]


#### Architecture
<img width="800" src="https://github.com/user-attachments/assets/7a2df17b-042e-4c5d-8712-add021e992c8"/>

#### UI
<div style="display:flex; width:200px;">
  <img width="200"  src="https://github.com/user-attachments/assets/4b053320-a386-43fc-ab87-6ead930ec09a"/>
  <img width="200" src="https://github.com/user-attachments/assets/d981de96-2247-4347-9dbb-f44e46547ada"/>
  <img width="200" src="https://github.com/user-attachments/assets/53620fe2-8d9c-4992-bdd8-1f2de8f5b616"/>
  <img width="200" src="https://github.com/user-attachments/assets/463cc742-d9f6-4560-804d-256e56661871"/>
</div>



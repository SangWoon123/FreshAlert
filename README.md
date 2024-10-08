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
<img width="600" src="https://github.com/user-attachments/assets/73ba9402-9685-4218-80a4-59006f455351"/>

#### UI
<div style="display:flex; width:200px;">
  <img width="200"  src="https://github.com/user-attachments/assets/4b053320-a386-43fc-ab87-6ead930ec09a"/>
  <img width="200" src="https://github.com/user-attachments/assets/42e7cd88-18d1-4192-b722-fb6233499df3"/>
  <img width="200" src="https://github.com/user-attachments/assets/53620fe2-8d9c-4992-bdd8-1f2de8f5b616"/>
  <img width="200" src="https://github.com/user-attachments/assets/45bf956a-0bbc-418e-a84e-c31178cad222"/>
</div>

## 변경 사항 (10.07)

---

## 기능

- **유제품**뿐만 아니라 **공산품**도 관리할 수 있는 **제품 입력 기능**을 추가하였습니다. 이를 통해 다양한 제품군에 대한 유통기한 및 반품 관리가 가능해졌습니다.
- 카테고리 엔티티를 추가하여 카테고리별 조회가 가능해 졌습니다.
    - 구성컬럼:
        - name: 카테고리명 (ex) CJ, 샘표, 오뚜기 등)
        - diary: 유통기한 관리일자 (ex) 3개월 전 → 3)

**실제 적용 예시**:

- **CJ 브랜드 공산품**의 경우, 유통기한 3개월 전 반품이 필요하도록 조회 기능이 적용되며, 이를 통해 체계적인 반품 관리가 가능합니다.

## 화면
 <img width="600"  src="https://github.com/user-attachments/assets/13f7a3fb-7088-4876-95b6-fe1ae25a41e4"/>


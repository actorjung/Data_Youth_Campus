# 즐기는 노인들 (데이터 청년 캠퍼스 1분반 4조)
- For Data Youth Campus(2023, SMU) in Korea.
- 'Indicator for old people(seniors) in Seoul'

## 1. 프로젝트 목적 및 배경
  ### 목적
  - 본 프로젝트는 노인(노인복지법,2022, 정의에 따름 : 만 65세 이상인 자)의 여가 생활 환경을 고려한 지표 제작을 목표로 합니다.
  - 해당 지표를 통해 서울 내 자치구별 노인들의 여가 환경에 대한 점수를 종합하여, 취약지역 및 우수 지역을 선정을 할 수 있습니다.
    우수 지역은 벤치 마킹할 점을 찾고, 취약 지역에서는 취약분야에 따른 효울적인 정책 수립 및 여가 장려를 목적으로 합니다.

  ### 배경
  - 현 대한민국은 1970년 대비 기대수명이 대폭 늘었고, 빠른 수준의 고령화가 진행되어 노인 인구의 비율이 높은 상태입니다.
    따라서, 여가문화를 노인층에 특화하여 분석할 필요가 있다고 판단하였습니다.
  - 국민행복도 증진은 국가적인 큰 목표이고, 여가생활과 사회연결정도가 삶의 만족도에 큰 영향을 준다는 연구 결과가 있습니다. 
    그러나 노인의 여가문화는 현재 TV시청 등 사회적으로 고립된 여가가 주를 이루었습니다. 사회적으로 연결된 여가활동이 확산될 필요가 있다 생각하여
    해당 분야에 집중하였습니다.  
  - 노인층에 대한 여가 관련 지표가 설문 결과이거나, 다양한 환경적 요소를 고려하지 못한 1차원적 지표인 경우가 많았습니다.
    여가와 관련된 다양한 환경 요소를 종합적으로 고려한 지표를 통해 자치구별 여가 수준을 한눈에 파악하고자 합니다.
  
## 2. About main.ipynb
 - ### Requirements
   - Main 파일은 ipynb 확장자로, 원할한 확인을 위해서는 Jupyter Notebook 이나, Jupyter Lab 사용을 권장드립니다.
   - Pyhthon version 3.9.x 
   - Used Libraries
     - Pandas
     - Matplotlib, Seborn
     - Numpy
     - OS
     - encoding UTF-8 or CP949
 - ### Used Python IDE
   - [Google Colab]
   - [JupyterLab & Notebook]
   - [Pycharm]
 - ### Variables
   각 csv 파일은 조원별 EDA 및 최종 전처리를 완료하였습니다.  
   Data_in_Code 폴더에서 확인 가능합니다.  
    -df_1 = 자치구별 노인 건강(음주 여부 구분).csv  
    -df_2 = 교통편의.csv  
    -df_3 = 자치구노인인구수_독거포함_최종.csv  
    -df_4 = 자치구별여가시설수_4차.csv  
    -df_5 = 자치구별 만족도.csv  
    -df_6 = 자치구별노인인구수비율.csv  
    -df_7 = 노인 월평균 소득+공시지가.csv
      &nbsp; </br>  
   2번부터, 여가시설수 -> 노인인구 -> 노인건강 -> 노인소득 ->  교통편의 순으로 코드가 존재하며,  
   각각의 .3. .4. 항목의 마지막줄에서 가중치 확인이 가능합니다.
    &nbsp;  </br>  
   프로젝트 내에서 채택한 OLS의 가중치는 그 중 .4. 항목입니다.
- ### others
    - code 내 회귀분석은 편의상 OLS로, 차원축소는 편의상 PCA로 표기하였습니다.
    - 8번 항목에서 채택한 OLS의 모델 검증 결과를 볼 수 있습니다. 설명력으로 사용한 지표는 F-statistic 과  Prob F-statistic입니다.

## 3. About Raw data
 - ### Sources
   - [서울시 열린데이터광장](https://data.seoul.go.kr/)
   - [대한민국 행복지도](http://www.happykorea.re.kr/)
 - ### Raw_data
   - [Raw_data] 폴더를 통해 프로젝트에 사용된 Raw_data 확인이 가능합니다.

## 4. About Processed Data
  - 모든 가공된 데이터는 csv 확장자로 저장되었습니다.
  - [Data_in_Code] 폴더에서 확인이 가능합니다.
  - [Processing] 폴더에서 전처리 과정이 확인 가능합니다.


## 5. 참고 (Refrences)
![image](https://github.com/Shaerrr/Leisure_Indicator_for_Oldmans_in-Seoul/assets/116930070/08449f10-9070-4d41-8ef8-ef6e10f90394)
 
## 6. 프로젝트 참여 인원 & Support
- 김형후 [GitHub](https://github.com/Shaerrr)/E-mail: dcfjk1234@naver.com
- 강재훈 
- 김소은
- 김현동
- 김화정
- 임주연
- 정우성
  

## 뷰의 크기 지정에 사용되는 단위

|단위|단위 표현|설명|
|:---|:---|:---|
|px|픽셀|화면 픽셀|
|dp 또는 dip|밀도 독립적 픽셀 <br> (density independent pixel)|160dpi 화면을 기준으로 한 픽셀 <br> 예) 1인치 당 160개의 점이 있는 디스플레이 화면에서 1dp는 1px와 같음. <br> 1인치 당 320개의 점이 있는 디스플레이 화면에서 1dp는 2px와 같음.|
|sp 또는 sip|축적 독립적 픽셀 <br> (scale independent pixel)|가변 글꼴을 기준으로 한 픽셀로 dp와 유사하나 글꼴의 설정에 따라 달라짐|
|in|인치|1인치로 된 물리적 길이|
|mm|밀리미터|1밀리미터로 된 물리적 길이|
|em|텍스트 크기|글꼴과 상관없이 동일한 텍스트 크기 표시|

주로 사용하는 단위는 **dp**

## 대표적인 레이아웃
|레이아웃 이름|설명|
|:---|:---|
|제약 레이아웃 <br> (Constraint Layout)|제약 조건(constraint) 기반 모델 <br> 제약 조건을 사용해 화면을 구성하는 방법 <br> 안드로이드 스튜디오에서 자동으로 설정하는 디폴트 레이아웃|
|리니어 레이아웃 <br> (Linear Layout)|박스(box) 모델 <br> 한 쪽 방향으로 차례대로 뷰를 추가하며 화면을 구성하는 방법 <br> 뷰가 차지할 수 있는 사각형 영역을 할당|
|상대 레이아웃 <br> (Relative Layout)|규칙(rule) 기반 모델 <br> 부모 컨테이너나 다른 뷰와의 상대적 위치로 화면을 구성하는 방법|
|프레임 레이아웃 <br> (Frame Layout)|싱글(single) 모델 <br> 가장 상위에 있는 하나의 뷰 또는 뷰 그룹만 보여주는 방법 <br> 여러 개의 뷰가 들어가면 중첩하여 쌓게 됨. 가장 단순하지만 여러 개의 뷰를 중첩한 후 각 뷰를 전환하여 보여주는 방식으로 자주 사용함|
|테이블 레이아웃 <br> (Table Layout)|격자(grid) 모델 <br> 격자 모양의 배열을 사용하여 화면을 구성하는 방법 <br> HTML에서 많이 사용하는 정렬 방식과 유사하지만 많이 사용하지는 않음|

## 외부 라이브러리를 불러와서 사용하는 경우
![ExternalLibrary](https://github.com/Kim-SuBin/Android_study/blob/master/img/ExternalLibrary.PNG)
<br> 외부 라이브러리를 불러와서 사용하는 경우 위의 사진과 같이 빨간 줄이 뜨는 것을 볼 수 있다.
<br> 이것을 없애기 위해서는 android를 선언한 xmlns가 필요하다.
<br> MainActivity에 대한 activity_main.xml :
~~~
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:layout_behavior="@string/appbar_scrolling_view_behavior"
    tools:context=".MainActivity"
    tools:showIn="@layout/activity_main">

    <android.support.v7.widget.RecyclerView
        android:layout_width="0dp"
        android:layout_height="0dp"
        android:id="@+id/recycler1"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</android.support.constraint.ConstraintLayout>
~~~

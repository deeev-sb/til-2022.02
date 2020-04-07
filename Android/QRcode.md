# QR code
#### 출처
생성 : https://park-duck.tistory.com/108?category=843507
<br> 스캔 : https://park-duck.tistory.com/109?category=843507
<br> 스캔 세로모드 : https://park-duck.tistory.com/110?category=843507
<br> 
<br> 
<br> 

### 기본 설정
1. build.gradle(Module:app) 파일에 아래 코드 추가
  ~~~
  implementation 'com.journeyapps:zxing-android-embedded:3.6.0'
  ~~~
![AddMoudle](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FbrHO2M%2FbtquAz6PNUM%2Flj5bDxiXzsRRNyxgLmaqX0%2Fimg.png)
2. AndroidManifest.xml 파일에 아래 코드 추가
  ~~~
  android:hardwareAccelerated="true"
  ~~~
![AddCode](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FbPuyvu%2FbtquA1BZuGg%2F2kLzCTVzmaeBvHHYLYQQo0%2Fimg.png)

### QR코드 생성
~~~
package com.example.qrcodegenerator;

import android.graphics.Bitmap;
import android.os.Bundle;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.common.BitMatrix;
import com.journeyapps.barcodescanner.BarcodeEncoder;

public class CreateQRActivity extends AppCompatActivity {
    private ImageView iv;
    private String text;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_qr);

        iv = (ImageView)findViewById(R.id.qrcode);
        text = "A";

        MultiFormatWriter multiFormatWriter = new MultiFormatWriter();
        try{
            BitMatrix bitMatrix = multiFormatWriter.encode(text, BarcodeFormat.QR_CODE,200,200);
            BarcodeEncoder barcodeEncoder = new BarcodeEncoder();
            Bitmap bitmap = barcodeEncoder.createBitmap(bitMatrix);
            iv.setImageBitmap(bitmap);
        }catch (Exception e){}
    }
}
~~~

### QR코드 스캔
~~~
package com.example.qrcodescan;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

public class ScanQRActivity extends AppCompatActivity {

    private IntentIntegrator qrScan;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scan_qr);
        // IntentIntegrator는 QR 코드를 사용하기 위한 클래스
        qrScan = new IntentIntegrator(this);
        qrScan.setOrientationLocked(false); // default가 세로모드인데 휴대폰 방향에 따라 가로, 세로로 자동 변경됩니다.
        qrScan.setPrompt("Sample Text!");
        qrScan.initiateScan();
    }

    // scan 결과값 처리
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        IntentResult result = IntentIntegrator.parseActivityResult(requestCode, resultCode, data);
        if(result != null) {
            if(result.getContents() == null) {
                Toast.makeText(this, "Cancelled", Toast.LENGTH_LONG).show();
                // todo
            } else {
                Toast.makeText(this, "Scanned: " + result.getContents(), Toast.LENGTH_LONG).show();
                // todo
            }
        } else {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }

}

~~~

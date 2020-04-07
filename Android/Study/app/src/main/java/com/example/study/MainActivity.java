package com.example.study;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void onButton1Clicked(View v){
        Toast.makeText(this, "버튼이 눌렸어요.", Toast.LENGTH_LONG).show(); // 버튼이 눌리면 Toast message가 뜸

        Intent intent = new Intent(this, menu.class);
        startActivity(intent);
    }

    public void onButton2Clicked(View v){ // 웹브라우저 앱을 띄우는 코드
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://m.naver.com")); // 주소를 바꾸면 다른 창을 띄움
        startActivity(intent);
    }

    public void onButton3Clicked(View v){ // 전화걸기로 연결해주는 코드
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("tel:010-1234-4321"));
        startActivity(intent);
    }

}

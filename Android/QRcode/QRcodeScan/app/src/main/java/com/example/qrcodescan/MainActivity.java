package com.example.qrcodescan;

import android.content.Intent;
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
        Toast.makeText(this, "버튼이 눌렸어요.", Toast.LENGTH_LONG).show(); // 버튼이 눌리면 Toast message 가 뜸

        Intent intent = new Intent(this, ScanQRActivity.class);
        startActivity(intent);
    }
}

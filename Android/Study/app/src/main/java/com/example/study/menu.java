package com.example.study;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class menu extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);
    }

    public void onBackButtonClicked(View v){
        Toast.makeText(this, "돌아가기 버튼 누름", Toast.LENGTH_LONG).show();

        finish(); // 현재 activity 종료
    }

}

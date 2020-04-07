package com.example.listview;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.widget.ListView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    private Context mContext;
    private ArrayList<String> array_mountain;
    private ListView mListView;
    private MountainAdapter mMountainAdapter;



    @Override

    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        this.mContext = getApplicationContext();



        mListView = (ListView) findViewById(R.id.list_mountain);



        // 데이터 생성

        array_mountain = new ArrayList<>();

        array_mountain.add("한라산");

        array_mountain.add("백두산");

        array_mountain.add("월출산");

        array_mountain.add("금강산");

        array_mountain.add("마니산");

        array_mountain.add("설악산");

        array_mountain.add("관악산");

        array_mountain.add("지리산");

        array_mountain.add("대둔산");

        array_mountain.add("도봉산");



        // 아답터 연결

        mMountainAdapter = new MountainAdapter(mContext, array_mountain);

        mListView.setAdapter(mMountainAdapter);

    }

}

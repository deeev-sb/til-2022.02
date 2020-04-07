package com.example.recyclerview;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.graphics.drawable.Drawable;
import android.os.Bundle;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    RecyclerView mRecyclerView = null ;
    RecyclerImageTextAdapter mAdapter = null ;
    ArrayList<ItemActivity> mList = new ArrayList<ItemActivity>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mRecyclerView = findViewById(R.id.recycler1) ;

        // 리사이클러뷰에 SimpleTextAdapter 객체 지정.
        mAdapter = new RecyclerImageTextAdapter(mList) ;
        mRecyclerView.setAdapter(mAdapter) ;

        // 리사이클러뷰에 LinearLayoutManager 지정. (vertical)
        mRecyclerView.setLayoutManager(new LinearLayoutManager(this)) ;

        // 아이템 추가.
        addItem(getResources().getDrawable(R.drawable.ic_account_box_black_36dp),
                "Box", "Account Box Black 36dp") ;
        // 두 번째 아이템 추가.
        addItem(getResources().getDrawable(R.drawable.ic_account_circle_black_36dp),
                "Circle", "Account Circle Black 36dp") ;
        // 세 번째 아이템 추가.
        addItem(getResources().getDrawable(R.drawable.ic_assignment_ind_black_36dp),
                "Ind", "Assignment Ind Black 36dp") ;

        mAdapter.notifyDataSetChanged() ;

    }

    public void addItem(Drawable icon, String title, String desc) {
        ItemActivity item = new ItemActivity();

        item.setIcon(icon);
        item.setTitle(title);
        item.setDesc(desc);

        mList.add(item);
    }
}

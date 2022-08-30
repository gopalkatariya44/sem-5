package com.example.intent;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    Button explicit;
    Button view_implicit;
    Button dial_implicit;
    Button call_implicit;
    Button send_implicit;
    Button send_to_implicit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        view_implicit = findViewById(R.id.view_implicit);
        dial_implicit = findViewById(R.id.dial_implicit);
        call_implicit = findViewById(R.id.call_implicit);
        send_implicit = findViewById(R.id.send_implicit);
        send_to_implicit = findViewById(R.id.send_to_implicit);

        explicit = findViewById(R.id.explicit);

        explicit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(getApplicationContext(), "Explicit", Toast.LENGTH_SHORT).show();
                Intent ex = new Intent(getApplicationContext(), MainActivity2.class);
                startActivity(ex);

            }
        });
        view_implicit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent im = new Intent(Intent.ACTION_VIEW);
                im.setData(Uri.parse("https://www.google.com"));
                startActivity(im);
            }
        });
        dial_implicit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent im = new Intent(Intent.ACTION_DIAL);
                im.setData(Uri.parse("tel:4444444444"));
                startActivity(im);
            }
        });
        call_implicit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent im = new Intent(Intent.ACTION_CALL);
                im.setData(Uri.parse("tel:4444444444"));
                startActivity(im);
            }
        });
        send_implicit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent sendIntent = new Intent();
                sendIntent.setAction(Intent.ACTION_SEND);
                sendIntent.putExtra(Intent.EXTRA_TEXT, "This is my text to send.");
                sendIntent.setType("text/plain");

                Intent shareIntent = Intent.createChooser(sendIntent, null);
                startActivity(shareIntent);
            }
        });
        send_to_implicit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(Intent.ACTION_SENDTO);
                Uri uri = Uri.parse("mailto:email@gmail.com");
                intent.setData(uri);
                intent.putExtra("subject", "my subject");
                intent.putExtra("body", "my message");
                startActivity(intent);
            }
        });
    }
}
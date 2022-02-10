# json 형태 그대로 html에 추가하기

```html
<pre style="border: 1px solid #000000"><code id="json-container"></code></pre>
<script>
    const data = {
      "kakao" : [
        {
          "name" : "라이언",
          "age" : 5
        },
        {
          "name" : "어피치",
          "age" : 5
        },
        {
          "name" : "죠르디",
          "age" : 3
        }
      ]
    }
    
    document.getElementById('json-container').innerHTML = JSON.stringify(data, null, 2);
</script>
```

### 🔗 참고
![https://cotyhamilton.com/how-to-pretty-print-json-in-html-with-javascript/](https://cotyhamilton.com/how-to-pretty-print-json-in-html-with-javascript/)

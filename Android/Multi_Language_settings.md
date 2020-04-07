# [Multi Language settings](https://lktprogrammer.tistory.com/144)

### Adding Korean String Resources
1. /app/res/ 경로에 문자열 리소스 폴더 생성 (폴더명은 values-국가코드)
여기서 생성될 폴더명은 values-ko
![add_directory](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FBQjIj%2Fbtqu9aftCrb%2Fhsws1WMobeKxKqsDntkNlk%2Fimg.png)
2. Project 모드에서 /app/src/main/res/values-ko/ 경로에 *Values resource file* 클릭 후 *string.xml* 파일 생성
![add_string.xml](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fbiv6cW%2FbtqvbHKdoEH%2FLZI8KG0SOvjFWnRV2rqv61%2Fimg.png)
3. string.xml 파일 내용을 아래 코드로 덮어쓰기
  ~~~
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
      <string name = "TEST">안녕하세요!!</string>
  </resources>
  ~~~

### Adding English String Resources
1. /app/res/ 경로에 문자열 리소스 폴더 생성 (폴더명은 values-en)
2. Project 모드에서 /app/src/main/res/values-en/ 경로에 *Values resource file* 클릭 후 *string.xml* 파일 생성
3. string.xml 파일 내용을 아래 코드로 덮어쓰기
  ~~~
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
      <string name = "TEST">Hello!!</string>
  </resources>
  ~~~

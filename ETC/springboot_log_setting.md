# properties로 Spring-Boot log를 설정해보자!

slf4j를 사용하는 경우 logging 설정을 통해 properties에 추가함으로써 설정을 할 수 있다. (xml을 굳이 설정하지 않아도 됨!)

```
# level 설정 (trace, debug, info, warn, error)
logging.level.root=info
# console 설정을 아래와 같이 하면 console에 아무 것도 뜨지 않음.
logging.pattern.console =
# file path 설정 (file name과 함께 사용 X)
logging.file.path=/var/log/test
# file name 설정 (file path와 함께 사용 X)
logging.file.name=/var/log/test/test.log
# file 크기 설정 (default=10MB)
logging.file.max-size=100MB
# file 보관 기간 설정 (default=7)
logging.file.max-history=365
# rolling 정책 (default=${LOG_FILE}.%d{yyyy-MM-dd}-%i.gz)
logging.pattern.rolling-file-name=${LOG_FILE}.%d{yyyy-MM-dd}-%i.log
```
만약 info와 error에 대해 분리해서 만들고 싶다면 xml을 생성해야 한다!

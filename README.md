# kookgi_11gi
2021년 6월 15일 개강 빅데이터 UI 전문가양성
***
# 자바 API  
https://docs.oracle.com/javase/8/docs/api/
***
# 크롤링시 406 에러가 발생될 경우
헤더 정보 사이트 => https://developers.whatismybrowser.com/useragents/explore/layout_engine_name/trident/  
header = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
***
# 톰캣 서버 실행속도가 느릴경우  
Servers 폴더의 context.xml 파일을 열고 &lt;Context&gt; 태그 내부에  
&lt;JarScanner scanClassPath="false"/&gt;를 입력한다.

https://www.wincher.com/blog/google-search-operators
http://devcoma.blogspot.com/2017/04/google-search-parameters-resources.html

#### Programmable search engine
Is a google product. I believe most of the seach parameters can be used with url parameters but there are no equivalence docs
https://developers.google.com/custom-search/docs/xml_results

### The important parameters. 
Igonore all the gobledegook encoded BS the server uses to track you
##### google could change this stuff but not likely in the near future.
<table>
    <tr>
        <th>param</th>
        <th>meaning</th>
        <th>regular use</th>
    </tr>
    <tr>
        <td><strong>q</strong></td>
        <td>each word must be found uses <strong>AND</strong></td>
        <td>Seperate words with '+'</td>
    </tr>
    <tr>
        <td><strong>oq</strong></td>
        <td>Any word must be found. Uses <strong>OR</strong></td>
        <td>Seperate words with '+'</td>
    <tr>
        <td><strong>eq</strong></td>
        <td>No word found. Uses <strong>NOT</strong></td>
        <td>Seperate words with '+'</td>
    </tr>
    <tr>
        <td><strong>site:</strong></td>
        <td>Not a seperate parameter. Include as part of q, eq, oq</td>
        <td>https://www.google.com/search?&q=site:google.com/finance+GME</td>
    </tr>
    <tr>
        <td><strong>-</strong></td>
        <td>Add to q string</td>
        <td>https://www.google.com/search?&q=google+urls+-presentation+-Console&oq=google+urls+-presentation+-Console</td>
    </tr>
</table>
https://www.google.com/search?&q=google+urls+-presentation+-Console&oq=google+urls+-presentation+-Console

### Embedding the site variable-- it is part of the q parameter
###### "Page created - February 5, 2021" inurl:facebook.com intitle:Home Improvement
https://www.google.com/search?
q="Page+created+-+February+5,+2021"+site:facebook.com+intitle:Home+Improvement
&oq="Page+created+-+February+5,+2021"+site:facebook.com+intitle:Home+Improvement
&start=0

### Generated from server- sending it back gets same results
https://www.google.com/search?q="Page+created+-+February+7,+2021"+inurl:facebook.com+intitle:Home+Improvement&oq="Page+created+-+February+7,+2021"+inurl:facebook.com+intitle:Home+Improvement&ie=UTF-8
https://www.google.com/search?q="Page+created+-+February+7,+2021"+inurl:facebook.com+intitle:Home+Improvement&oq="Page+created+-+February+7,+2021"+inurl:facebook.com+intitle:Home+Improvement&ie=UTF-8&start=0

### possible extra params
&client=ubuntu&channel=fs
&ie=utf-8
&oe=utf-8

# Bing
"Page created - February 7, 2021" site:facebook.com intitle: Home Improvement
"Page created - February 7, 2021" site:facebook.com intitle: Home Improvement
"Page created - February 7, 2021" site: facebook.com intitle: Home Improvement
https://www.bing.com/search?
q="Page 20created 20- 20February 207 2C 202021" 20site:facebook.com 20intitle:Home 20Improvement
&qs=n
&form=QBRE
&sp=-1
&pq="page 20created 20- 20february 205 2C 202021" site:facebook.com 20intitle:home 20improvement
&sc=0-76
&first=0

# Yahoo
"Page created - February 7, 2021" site:facebook.com intitle: Home Improvement
https://search.yahoo.com/search
p="Page+created+-+February+8 2C+2021"+site:facebook.com+intitle:+Home+Improvement
&fr2=sb-top
&fr=yfp-t
&fp=1

https://search.yahoo.com/search?p="Page+created+-+February+5,+2021"+site:facebook.com+intitle:+Home+Improvement&b=0
&fp=1
&fr2=sa-gp-search
&n=30

https://search.yahoo.com/search?p=%22Page+created+-+February+5%2C+2021%22+site%3A+facebook.com+intitle%3A+Home+Improvement&b=0
&fr2=sb-top


### Yahoo next
https://search.yahoo.com/search?p="Page+created+-+February+5,+2021"+site:facebook.com+intitle:+Home+Improvement
&b=11
&pz=10
&bct=0
&xargs=0

https://search.yahoo.com/searchu?
p="Page+created+-+February+5,+2021"+site:facebook.com+intitle:+Home+Improvement
&pz=10
&bct=0
&b=21
&pz=10
&bct=0
&xargs=0




<a class="next" 
href="
https://search.yahoo.com/search;
_ylt=Awr9BNYYLyFgf7kArNJXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZANDMDkzNF8xBHNlYwNwYWdpbmF0aW9u?
p="Page+created+-+February+5,+2021"+site:facebook.com+intitle:+Home+Improvement
&amp;fr=yfp-t
&amp;fr2=sb-top
&amp;fp=1
&amp;b=11
&amp;pz=10
&amp;bct=0
&amp;xargs=0" 
referrerpolicy="unsafe-url">

<a href="
/search?
q=&amp;
&amp;biw=763
&amp;bih=895
&amp;ei=MDEhYOuIKdKPtAaDuZigCQ
&amp;start=10
&amp;sa=N
&amp;ved=2ahUKEwjr4NPGp9ruAhXSB80KHYMcBpQQ8NMDegQIGhBI"



<a 
href=
"/search?
q= &amp ;
&amp;biw=1755
&amp;bih=895
&amp;ei=mDAhYKn8EcettQbu6pGwBA
&amp;start=20
&amp;sa=N
&amp;ved=2ahUKEwipqP_9ptruAhXHVs0KHW51BEY4ChDw0wN6BAgJEEg" 
### Yahoo links are embedded in
'https://r.search.yahoo.com/_ylt=Awr9IMzatyFgFAYAJ3tXNyoA;_ylu=Y29sbwNncTEEcG9zAzQEdnRpZAMEc2VjA3Ny/RV=2/RE=1612851290/RO=10/RU=https%3a%2f%2fwww.facebook.com%2fmonilove1993%2f/RK=2/RS=gMY2nOif0zfGmP2Hehw8LTljIaM-'

<a href="
https://search.yahoo.com/search?
p=%22Page+created+-+February+5%2C+2021%22+site%3A+facebook.com+intitle%3A+Home+Improvement
&amp;b=41
&amp;pz=10
&amp;bct=0
&amp;xargs=0"

 referrerpolicy="unsafe-url" title="Results 41-50">5</a>


### originals from DT
inurl:bbb.org "Accredited Since:2/5/2021" intitle:Construction

intext:Proudly created with Wix.com "construction"
this 1 i have to change the time created to 24 hours or less


https://www.bing.com/search?q="Page+created+-+February+7 2C+2021"+site:+facebook.com+intitle:+Home+Improvement
&form=QBLH
&sp=-1
&pq=
&sc=8-0
&qs=n
&sk=
&cvid=4164FF4B44404FB2BDCD0F6CC0B87213

### Bing next
https://www.bing.com/search?
q="Page+created+-+February+5 2c+2021"+site:+facebook.com+intitle:+Home+Improvement
&first=12
&FORM=PORE



### The othere 2
https://www.bing.com/search?q=fred
&form=QBLH
&sp=-1
&pq=fred
&sc=8-4
&qs=n&sk=&cvid=7CB8FB843D1F42BE8EE5878EC76A3EB4



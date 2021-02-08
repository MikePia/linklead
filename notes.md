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
"Page created - February 7, 2021" site: facebook.com intitle: Home Improvement
https://www.bing.com/search?
q=%22Page%20created%20-%20February%207%2C%202021%22%20site%3Afacebook.com%20intitle%3AHome%20Improvement
&qs=n
&form=QBRE
&sp=-1
&pq=%22page%20created%20-%20february%205%2C%202021%22%20site%3Afacebook.com%20intitle%3Ahome%20improvement
&sc=0-76
&sk=
&cvid=D6BA1A570F0B4D0582EB5A3346B5C5A6

### originals from DT
inurl:bbb.org "Accredited Since:2/5/2021" intitle:Construction

intext:Proudly created with Wix.com "construction"
this 1 i have to change the time created to 24 hours or less


https://www.bing.com/search?q=%22Page+created+-+February+7%2C+2021%22+site%3A+facebook.com+intitle%3A+Home+Improvement
&form=QBLH
&sp=-1
&pq=
&sc=8-0
&qs=n
&sk=
&cvid=4164FF4B44404FB2BDCD0F6CC0B87213

### Bing next
https://www.bing.com/search?
q=%22Page+created+-+February+5%2c+2021%22+site%3a+facebook.com+intitle%3a+Home+Improvement
&first=12
&FORM=PORE

https://www.bing.com/search?q=%22Page%20created%20-%20February%205%2C%202021%22%20site%3A%20facebook.com%20intitle%3A%20Home%20Improvement&pq=%22page%20created%20-%20february%207%2C%202021%22%20site%3A%20facebook.com%20intitle%3A%20home%20improvement&qs=n&form=QBRE&sp=-1
&sc=0-78&sk=&cvid=84AE0F1374034EFABD9AD6985649DFFB

https://www.bing.com/search?
q=%22Page+created+-+February+5%2c+2021%22+site%3a+facebook.com+intitle%3a+Home+Improvement
&first=22&FORM=PERE1

 'https://www.bing.com/search?
 q=%22Page%20created%20-%20February%205%2C%202021%22%20site%3A%20facebook.com%20intitle%3A%20Home%20Improvement&pq=%22page%20created%20-%20february%207%2C%202021%22%20site%3A%20facebook.com%20intitle%3A%20home%20improvement
 &qs=n
 &form=QBRE
 &sp=-1'


### The othere 2
https://www.bing.com/search?q=fred
&form=QBLH
&sp=-1
&pq=fred
&sc=8-4
&qs=n&sk=&cvid=7CB8FB843D1F42BE8EE5878EC76A3EB4



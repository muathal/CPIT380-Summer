def header(title):
    htmlHader = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>%s</title>
    </head>
    """ % title
    return htmlHader
def body(header1,header20,header21,header22,parah1,pararh20,pararh21,pararh22):
    htmlBody ="""
    <body>
    <h1>%s</h1>
    <img src="../img/muath.jpg" 
    width="250"
    height="280">
    <p>%s</p>
    <h2>%s</h2>
    %s
    <img src="../img/cats.jpg"
    width="250"
    height="280">

    <h2>%s</h2>
    <p>%s</p>
    <img src="../img/gothic plate armour.jpeg"
    width="250"
    height="280">
    <h2>%s</h2>
    <p>%s</p>
    </body>
    </html>
    """ % (header1,parah1,header20,pararh20,header21,pararh21,header22,pararh22)
    return htmlBody
header1 = "Welcome to Muath Alhuumi's personal blog"
para1 = """good morning, good afternoon and good evening my fellow visitor
In eid Al-Adha I took a selfie with my cousin's cocktail
"""
header2 = "Hobbies and field of interest"
para20 = """<ul>
<li>playing vidoegames</li>
<li>cooking</li>
<li>baking</li>
<li>psychology and sociology</li>
<li>data science and AI</li>
<li>observing</li>
</ul>
"""
header3 = "Family of Cats"
para21 = """
While I was waiting for my family outside the mall I found a family of cats.
At first it was one cat after i got close to it the whole family ambushed me.
"""
header4 = "gothic plate armour"
para22 = """
when I was a young I always loved the medieval and late medieval age, the armours and the weapons.
The armour in the photo is form the late ages in what now called germany. 
"""
html = header("Muath Alhurtumi 2238766")
html += body(header1,header2,header3,header4,para1,para20,para21,para22)
file = open("muath.html","wt")
file.write(html)
file.close()
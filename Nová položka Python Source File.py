from flask import Flask, render_template_string
import gin_s_tonicom as data

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Kokteily</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">

<style>

body{
    font-family:'Poppins', sans-serif;
    margin:0;
    background:linear-gradient(#50C878);
}

/* HEADER */
.header{
    text-align:center;
    padding:30px;
    color:white;
}

.header h1{
    margin:0;
    font-size:40px;
}

/* GRID */
.grid{
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(240px,1fr));
    gap:25px;
    padding:30px;
}

/* CARD */
.card{
    background:white;
    border-radius:15px;
    overflow:hidden;
    box-shadow:0 8px 20px rgba(0,0,0,0.2);
    transition:0.3s;
    position:relative;
}

.card:hover{
    transform:translateY(-8px) scale(1.03);
    box-shadow:0 15px 30px rgba(0,0,0,0.3);
}

/* IMAGE */
.card img{
    width:100%;
    height:220px;
    object-fit:cover;
}

/* NAME */
.name{
    padding:15px;
    text-align:center;
    font-weight:600;
    font-size:18px;
}

/* COLOR STRIP */
.card::after{
    content:"";
    height:5px;
    width:100%;
    position:absolute;
    bottom:0;
    left:0;
    background:linear-gradient(90deg,#ff758c,#ff7eb3,#84fab0,#8fd3f4);
}

/* FOOTER */
.footer{
    text-align:center;
    padding:20px;
    color:white;
    opacity:0.9;
}

</style>
</head>

<body>

<div class="header">
    <h1>🍹 Nápoje ktoré ponúkame 🍹</h1>
    <p>Objavťe svoje obľúbené drinky</p>
</div>

<div class="grid">
{% for i in range(names|length) %}
    <div class="card">
        <img src="{{ images[i] }}">
        <div class="name">{{ names[i] }}</div>
    </div>
{% endfor %}
</div>

<div class="footer">
    Flask Cocktail App ✨
</div>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(
        HTML,
        names=data.meno,
        images=data.obr
    )

if __name__ == "__main__":
    app.run(debug=True)
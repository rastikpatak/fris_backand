from flask import Flask, render_template_string
import gin_s_tonicom as data

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Kokteily</title>

<style>
body{
    font-family: Arial;
    background:#98FF98;
    padding:20px;
}

h1{
    text-align:center;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(220px,1fr));
    gap:20px;
}

.card{
    background:white;
    border-radius:12px;
    overflow:hidden;
    box-shadow:0 3px 8px rgba(0,0,0,0.2);
}

.card img{
    width:100%;
    height:200px;
    object-fit:cover;

}

.name{
    padding:10px;
    font-weight:bold;
    text-align:center;
}
</style>
</head>

<body>

<h1>🍹 Kokteily</h1>

<div class="grid">
{% for i in range(names|length) %}
    <div class="card">
        <img src="{{ images[i] }}">
        <div class="name">{{ names[i] }}</div>
    </div>
{% endfor %}
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
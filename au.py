from flask import Flask
import gin_s_tonicom as gin
#print(gin)
mena =[]
print(gin.meno)
print(gin.obr)
image = []

app = Flask(__name__)
#def vytiahni_mena(gin):
#    return image.append[::2]
#mena = vytiahni_mena(gin)
#print(mena)
#print(gin[1::2])
@app.route("/")
def hello():
    return """
Hello, World!
"""
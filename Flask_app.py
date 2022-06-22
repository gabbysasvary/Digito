from flask import Flask
from rhino3dm import *
import rhino3dm
import ghhops_server as hs
app = Flask(__name__)

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/pointat",
    name="PointAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate", default =4.0),
    ],
    outputs=[
        hs.HopsPoint("p", "p", "Point on curve at t")
    ],
)
def pointat(curve: rhino3dm.Curve, t):
    return curve.PointAt(t)


if __name__ == "__main__":
    app.run()

@app.route('/')
def hello_world():
    return 'Hello from Gabby from UNSW CODE'
# GoogleMapsTrafficPrediction


Given a set of input roadid, direction, day, time, and status you can train the model:
Ex: http://ec2-35-161-32-246.us-west-2.compute.amazonaws.com:5000/train?roadid=10&direction=2&day=3&time=4&status=6


You are able to use the model to predict the status of the traffic by providing the roadid, direction, day, and time:
Ex: http://ec2-35-161-32-246.us-west-2.compute.amazonaws.com:5000/predict?roadid=10&direction=2&day=3&time=4
  
The machine learning algorithm uses polynomial interpolation to fit the roadid, direction, day and time to the status. 

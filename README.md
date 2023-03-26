
# STSS: Smart Traffic Signal System

The project aims at getting traffic volume from left and right lanes and thus deciding the "GREEN-LIGHT" time alloted to each lane.

It uses pre-trained Tensorflow object detection model to infer vehicle count in each of the lane and use that inferred data to get approximate traffic volume on each side of the road.

Depending on the volume of each lanes the green light time is updated such that lane with high traffic volume gets assigned more green light time as compared to lane with less traffic

## Installation

Clone the repo to your local
Navigate to cloned folder and install requirements.txt

Pre-requirements:
Make sure python is installed on your system

```bash
  cd my-project
  pip install -r requirements.txt
```
Install ray serve
```bash
  pip install "ray[serve]"
```

## Deployment

The project will be deployed on "ray-serve"

Start ray cluster
```bash
  ray start --head
```
Stop ray
```bash
  ray stop
```

To deploy the model, run deploy_ray_model.py script

```bash
  python3 deploy_ray_model.py
```

Once the deployment is successfull, now lets start Front End to make request for inference.
For this we will be using simple python server to run our web page.

Navigate to UI folder and execute below command to spin up new web-server. Now in browser open address http://127.0.0.1:8081/
```bash
  python3 -m http.server 8081 --bind 127.0.0.1
```
 On UI interface enter sample image URL's for left and right lanes and click submit button.

Wait for model to analyse and return data.
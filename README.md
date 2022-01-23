# Phishing-URL-detector

<img src="https://media.istockphoto.com/photos/phishing-attack-picture-id1253294358?s=612x612" alt="drawing" width="600"/>

This is an API that returns if an URL is phishing or not just giving the string in the frontend what is made for.
It is made in the following way:

1. A MySQL database with more than 11.000 URL for the request.
2. A ML prediction model which says if an URL direction is phishing or not with an accuracy of 76%.
3. After the prediction, the URL and the result will be saved in the database for a quicker request.

Resources:
- http://archive.ics.uci.edu/ml/datasets/Phishing+Websites
- https://data.mendeley.com/datasets/72ptz43s9v/1
- https://www.sciencedirect.com/science/article/pii/S2352340920313202

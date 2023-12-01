# Sentinel2
A backend DevOps project for Sentinel 2

Here's the Sentinel 2 API developed using Fastapi, it also contains the dockerization and the yaml files to deploy it in kubernetes.

It is deployed in localhost and has 2 endpoints:

Use /attributes to get the attributes of an image
Use /thumbnail to convert the image to a PNG

The browser may not let a download of the PNG image in the /Thumbnail endpoint but it is generated in the folder with the output_thumbnail.png name
With 2 hours i couldn't improve more the endpoint and i could not optimize the code or make the visual parts more pleasant

Thank you!

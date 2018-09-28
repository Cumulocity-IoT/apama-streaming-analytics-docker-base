# Rebuilding official Apama images with new base OSs

This Dockerfile uses multi-stage builds to rebuild Apama correlator and builder images from other base OS images.

## Using the Dockerfile

Context is irrelevant for this Dockerfile, it's all contained within the Dockerfile and the original images that are being rebuilt from. The Dockerfile exposes several build arguments which can be used to tailor your new images:

* `BASE_OS` - This must always be set to the docker repository and tag of the base OS you want to use
* `APAMA_VERSION` - This must always be set to the 2-digit version of Apama which is being rebuilt
* `APAMA_IMAGE` - By default the Dockerfile will use the `${APAMA_VERSION}` correlator image from Docker Store. To rebuild the builder image, or to pull images from another location, set this to the full `registry/repository:image` of the source image to use.

For example, to rebuild the 10.3 Docker Store Apama image using the latest Ubuntu as a base image you would run:

    docker build -t apama-correlator:ubuntu --build-arg BASE_OS=ubuntu --build-arg APAMA_VERSION=10.3 -f https://raw.githubusercontent.com/SoftwareAG/apama-streaming-analytics-docker-base/master/Dockerfile .

Alternatively, to rebuild the Apama builder image from store you would run:

    docker build -t apama-builder:ubuntu --build-arg BASE_OS=ubuntu --build-arg APAMA_VERSION=10.3 --build-arg APAMA_IMAGE=store/softwareag/apama-builder:10.3 -f https://raw.githubusercontent.com/SoftwareAG/apama-streaming-analytics-docker-base/master/Dockerfile .



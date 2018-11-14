# Rebuilding official Apama images with new base OSs

This Dockerfile uses multi-stage builds to rebuild Apama correlator and builder images from other base OS images.

## Using the Dockerfile

Context is irrelevant for this Dockerfile, it's all contained within the Dockerfile and the original images that are being rebuilt from. The Dockerfile exposes several build arguments which can be used to tailor your new images:

* `BASE_OS` - This must always be set to the docker repository and tag of the base OS you want to use
* `APAMA_VERSION` - This must always be set to the 2-digit version of Apama which is being rebuilt
* `APAMA_IMAGE` - By default the Dockerfile will use the `${APAMA_VERSION}` correlator image from Docker Store. To rebuild the builder image, or to pull images from another location, set this to the full `registry/repository:image` of the source image to use.

For example, to rebuild the 10.3 Docker Store Apama image using the latest Ubuntu as a base image you would run:

    docker build -t apama-correlator:ubuntu --build-arg BASE_OS=ubuntu --build-arg APAMA_VERSION=10.3 https://github.com/SoftwareAG/apama-streaming-analytics-docker-base.git

Alternatively, to rebuild the Apama builder image from store you would run:

    docker build -t apama-builder:ubuntu --build-arg BASE_OS=ubuntu --build-arg APAMA_VERSION=10.3 --build-arg APAMA_IMAGE=store/softwareag/apama-builder:10.3 https://github.com/SoftwareAG/apama-streaming-analytics-docker-base.git

## Testing the images

The dockerfile also comes with a second docker project which will test the images built be the first one in the `tests` directory. To use it you should build a second image setting the tags of your images as arguments to that build process. That build file has two build arguments:

* `APAMA_IMAGE` - The tag of the apama-correlator image. It defaults to the image from store.
* `APAMA_BUILDER` - The tag of the apama-builder image. It defaults to the image from store.

To run these tests you'll probably want to check out the git repository and run it from the working copy. For example, if you just rebuilt the correlator image you could run it like:

    docker build -t test-ubuntu-correlator --build-arg APAMA_IMAGE=apama-correlator:ubuntu tests

If the build completes successfully then the tests have passed.
______________________

These tools are provided as-is and without warranty or support. They do not constitute part of the Software AG product suite. Users are free to use, fork and modify them, subject to the license agreement. While Software AG welcomes contributions, we cannot guarantee to include every contribution in the master project.	

Contact us at [TECHcommunity](mailto:technologycommunity@softwareag.com?subject=Github/SoftwareAG) if you have any questions.

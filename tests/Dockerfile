ARG APAMA_VERSION=10.3
ARG APAMA_BUILDER=store/softwareag/apama-builder:${APAMA_VERSION}
ARG APAMA_IMAGE=store/softwareag/apama-correlator:${APAMA_VERSION}

FROM ${APAMA_BUILDER}
COPY --chown=sagadmin:sagadmin . ${APAMA_WORK}/tests
RUN cd ${APAMA_WORK}/tests; ant build
RUN cd ${APAMA_WORK}/tests; engine_deploy --outputDeployDir TestBuilderImage/Input/project project
RUN cd ${APAMA_WORK}/tests; engine_package -o test.cdp test.jar test.mon
RUN cd ${APAMA_WORK}/tests; cp test.jar test.mon TestBuilderImage/Input/
RUN cd ${APAMA_WORK}/tests; pysys run TestBuilderImage
FROM ${APAMA_IMAGE}
COPY --chown=sagadmin:sagadmin . ${APAMA_WORK}/tests
RUN cd ${APAMA_WORK}/tests; pysys run TestCorrelatorImage

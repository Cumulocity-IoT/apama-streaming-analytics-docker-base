ARG BASE_OS=base
ARG APAMA_VERSION=10.3
ARG APAMA_IMAGE=store/softwareag/apama-correlator:${APAMA_VERSION}
FROM ${APAMA_IMAGE} as orig

FROM ${BASE_OS}
MAINTAINER SoftwareAG

SHELL ["/bin/bash", "-c"]
RUN groupadd -g 1724 sagadmin && useradd -d /opt/softwareag --no-create-home -g 1724 -u 1724 sagadmin

COPY --from=orig --chown=sagadmin:sagadmin /opt/softwareag /opt/softwareag

ENV \
		 SAG_HOME=/opt/softwareag \
		 APAMA_HOME=/opt/softwareag/Apama \
		 APAMA_WORK=/apama_work \
		 APAMA_LIBRARY_VERSION=${APAMA_VERSION}

ENV \
		 LD_LIBRARY_PATH="${APAMA_HOME}/lib:${APAMA_WORK}/lib:${APAMA_HOME}/third_party/python/lib:$SAG_HOME/UniversalMessaging/cplus/lib/x86_64" \
		 PATH="${APAMA_HOME}/bin:${APAMA_HOME}/third_party/apache_ant/bin:${APAMA_HOME}/third_party/python/bin:${SAG_HOME}/jvm/jvm/jre/bin:${SAG_HOME}/jvm/jvm/bin:$PATH" \
		 PYTHONPATH=${APAMA_HOME}/third_party/python/lib/python3.6/site-packages \
		 ANT_HOME="/opt/softwareag/Apama/third_party/apache_ant"

RUN ldconfig

WORKDIR ${APAMA_WORK}
RUN chown sagadmin:sagadmin ${APAMA_WORK}

USER sagadmin:sagadmin
CMD ["correlator"]

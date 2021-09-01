FROM jupyter/datascience-notebook:python-3.9.6

# Environment: Udacity AI Trading, Python 3.6
## Install Udacity AI environment
## Doc: https://sites.northwestern.edu/summerworkshops/resources/adding-python-3-to-jupyter-notebooks/
RUN conda create -y -n UdacityAI python=3.6 ipykernel && \
    source activate UdacityAI && \
    ipython kernel install --name UdacityAI --user


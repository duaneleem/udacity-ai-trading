FROM jupyter/datascience-notebook:python-3.9.6

# Environment: Udacity AI Trading, Python 3.6
## Install Udacity AI environment
## Doc: https://sites.northwestern.edu/summerworkshops/resources/adding-python-3-to-jupyter-notebooks/
RUN conda create -y -n UdacityAI python=3.6 ipykernel && \
    source activate UdacityAI && \
    ipython kernel install --name UdacityAI --user

## Linux Deps
RUN apt-get update -y && \
  apt-get install graphviz -y

## TODO: Install Python Deps
RUN pip3 install \
  # Data Science
  numpy \
  pandas \
  alphalens \
  tqdm \
  # Machine Learning
  sklearn \
  torch torchvision \
  ## NLP
  nltk \
  scikit-learn



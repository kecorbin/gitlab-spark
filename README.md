# gitlab-spark

webhook endpoint for gitlab + cisco spark

# Installation

```
git clone https://github.com/kecorbin/gitlab-spark
cd gitlab-spark
docker build -t gitlab-spark .
docker run -p 5000:5000 gitlab-spark
```

# Configuration

You can now configure gitlab to send webhook events to the machine you installed
the receiver on.  

Currently only the following events are supported:

* Push
* issues


# TODO

* pipeline events
* build events
* comment events
* merge request events

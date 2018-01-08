# gitlab-spark

webhook endpoint for gitlab + cisco spark

Full documentation on gitlab webhooks are available [here](https://docs.gitlab.com/ce/user/project/integrations/webhooks.html)
# Installation

### From Source
```
git clone https://github.com/kecorbin/gitlab-spark
cd gitlab-spark
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Using Docker

```
docker run -p 5000:5000 kecorbin/gitlab-spark
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

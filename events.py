import os

def event_handler(msg):
    """
    receives gitlab message and executes the appropriate formatter
    """

    if os.getenv("DEBUG"):
        print(msg)

    handler_map = {
        'push': push_formatter,
        'issue': issue_formatter,
        'pipeline': pipeline_formatter,
        'note': note_formatter,
        'build': builds_formatter,
        'merge_request': merge_request_formatter
    }

    object_kind = msg['object_kind']
    message = handler_map[object_kind](msg)
    return message


def push_formatter(msg):
    message = "In [{}]({}), {} pushed just pushed commit(s)\n".format(msg['project']['path_with_namespace'],
                                                                    msg['project']['git_http_url'],
                                                                    msg['user_name'])
    for commit in msg['commits']:
        message += "* [{}]({})\n".format(commit['message'], commit['url'])
    return message

def issue_formatter(msg):
    issue = msg['object_attributes']
    message = "In [{}]({}), {} just {} an issue.\n".format(msg['project']['path_with_namespace'],
                                                         msg['project']['git_http_url'],
                                                         msg['user']['username'],
                                                         issue['state'])

    message += "* [{}]({})\n".format(issue['title'], issue['url'])
    if msg['labels']:
        message += " : Labels: "
        for l in msg['labels']:
            message += "{} ".format(l['title'])

    return message

def pipeline_formatter(msg):
    return None

def note_formatter(msg):
    return "A note event occured"

def builds_formatter(msg):
    build = msg
    status = build['build_status']
    build_id = build['build_id']
    stage = build['build_stage']
    repo = build['project_name']
    repo_url = build['repository']['homepage']
    sparkmsg = ""
    sparkmsg += "### Build update for build {}\n".format(build_id)
    sparkmsg += "\n\n**Repostory**: [{}]({})".format(repo, repo_url)
    sparkmsg += "\n\n**Status**: {}".format(status)
    sparkmsg += "\n\n**Stage**: {}".format(stage)

    return sparkmsg


def merge_request_formatter(msg):
    # glean important information from incoming message
    mr = msg['object_attributes']
    source_branch = mr['source_branch']
    target_branch = mr['target_branch']
    user = msg['user']['username']
    source_repo = mr['source']['path_with_namespace']
    target_repo = mr['target']['path_with_namespace']
    state = mr['state']
    title = mr['title']
    url = mr['url']

    # format spark message
    message = ""
    message += "In {}.".format(target_repo)
    message += "A [pull request]({}) was {} by {}".format(url, state, user)
    return message

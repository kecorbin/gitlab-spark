
def event_handler(msg):
    """
    receives gitlab message and executes the appropriate formatter
    """
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
    print(msg)
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
    print msg


handler_map = {
    'push': push_formatter,
    'issue': issue_formatter,
    'pipeline': pipeline_formatter
}

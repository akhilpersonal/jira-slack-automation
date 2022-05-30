# This will create jira issue using jira-python module and publish message to a slack channel.

- jira hosted on local host. 
- jira credentials are being fetched from system env variables. 
- It will create ticket then transition to a status.
- based on the error handling message will be published to a slack channel.
- Slack integration  ref -> https://api.slack.com/messaging/sending
    - create slack app
    - generate token 
    - permission slack app to a workspace , channel 
    - slack message would be either "issue created with issue key" or "an error in creation".


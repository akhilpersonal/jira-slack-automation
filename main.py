#Initial imports for jira , slack module
from jira import JIRA,JIRAError
from slack_sdk import WebClient
import os
from slack_sdk.errors import SlackApiError


# We declare the initial variables and pass them to the client
# jira user id , passwrd will fetch from system env variables

user = os.environ.get('JIRA_USER')
password= os.environ.get('JIRA_PASSWORD')

jira = JIRA('http://localhost:8080',basic_auth=(user, password))

ticketdata = {
  "texts": ("This is the best ticket."," have a nice day."),
  "error": "There has been an error :"
}

#This function creates the Jira ticket
def trigger(tickedata):

    try:

        new_issue = jira.create_issue(project='FUN',
                                      summary='The most fun ticket of all time',
                                      description= (''.join(ticketdata['texts'])),
                                      issuetype={'name': 'automation'})
        final = "Issue {} created with the following decription.\n".format(new_issue) + \
                ''.join(ticketdata['texts'])
        print(final)

        # newly created issue is transitioning to In Progress state
        print("Starting Issue transition")
        transition = jira.transition_issue(new_issue, '41')
        print('Newly created issue {} transition to status InProgress'.format(new_issue))
        slack_integration(final)

    except JIRAError as e :
        final = ticketdata['error']
        print(final,e.text)
        slack_integration(final + e.text)

    return final

#Funtion for slack messaging
def slack_integration(final):

    try :

        slack_bot = WebClient(token=os.environ.get("SLACK_AUTH"))
        slack_bot.chat_postMessage(channel='#automation',text=final)
        print("Message published to slack channel #automation")
    except  SlackApiError as e:
        print("Publishing messgae to slack channel is failied due to : {}".format(e.response))

if __name__ == "__main__":
    trigger(ticketdata)




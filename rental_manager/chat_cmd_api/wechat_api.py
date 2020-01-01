"""
use as a messenger to push notification/or send request command;
make sure all manager commands are stored;
make sure all clients requests are stored;
"""
import itchat


# configs:
FRIENDS = dict()  # itchat.get_friends(update=True)[0:]


def _search_friends(user_name=None, account=None, nick_name=None):
    if user_name:
        results = itchat.search_friends(userName=user_name)
    elif account:
        results = itchat.search_friends(wechatAccount=account)
    elif nick_name:
        results = itchat.search_friends(nickName=nick_name)
    else:
        raise ValueError("please at least input 1 search criteria.")

    return results


@itchat.msg_register(itchat.content.TEXT)
def auto_response(message):
    message_info = dict()
    message_info['text'] = message.text
    message_info['content'] = message.content
    message_info['sender'] = message.fromUserName
    message_info['recipient'] = message.toUserName

    itchat.send_msg('response', message_info['sender'])
    print('receiving command ', message_info)


if __name__ == '__main__':
    itchat.auto_login()
    import pprint

    pprint.pprint(itchat.get_friends(update=True))
    # results = itchat.search_friends(wechatAccount='')
    # print(results)
    # itchat.send_msg('hello ', account[0]['UserName'])
    itchat.run()



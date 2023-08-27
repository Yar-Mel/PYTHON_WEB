# from personal_assistant.src import setup
# import pkg_resources


class StartText:
    
    # Take name and version from METADATA
    # name = pkg_resources.get_distribution('willy').project_name
    # version = pkg_resources.get_distribution('willy').version
    
    title = '---HELLO---'
    text = f"I'M Willy ASSISTANT v1.0.*"
    greetings = 'NICE TO MEET YOU!'

    start_message = \
    '\n{:^40}\n{:^40}\n'.format(title, '-'*40)\
    +'|{:^38}|\n'.format(text)\
    +'|{:^38}|\n{:^40}\n'.format(greetings, '-'*40)

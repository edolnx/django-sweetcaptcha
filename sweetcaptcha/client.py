"""
sweetcaptcha
~~~~~~~~~~~~

A package made to easily integrate sweet captchas in your forms.

You can use the get_html and check functions to generate and validate sweet
captchas.  Alternatively you can use the wtforms.fields.Field classes in
sweetcaptcha.sweetcaptchawt.

This module is executable.  Provide your app_id and app_key on the commandline
to see the results of get_html
"""
import requests

SWEETCAPTCHA_API = 'https://sweetcaptcha.com/api'


def get_html(app_id, app_key, is_auto_submit=None, language=None):
    """Fetch html for a sweetcaptcha.


    get_html(app_id, app_key, [is_auto_submit], [language]) -> str

    :param app_id: your app id (string)
    :param app_key: your app key (string)
    :param is_auto_submit: when "1" will auto submit the form the widget is
    embedded within on user solve (optional, string)
    :param language: language code (string, optional), i.e FR (French),
    i.e RU (Russian).  Overrides the default language set for the application to
    support multilingual websites, will fallback to app's default if a
    translation is not available, , should be UPPER CASE 2 CHARS
    :return: HTML code to be implemented within your FORM tag (before the
    submit button)
    """
    data = dict(
                platform='api',
                method='get_html',
                app_id=app_id,
                app_key=app_key,
                )
    if is_auto_submit:
        dict['is_auto_submit'] = 1
    if language:
        dict['language'] = language.upper()
    fo = requests.post(SWEETCAPTCHA_API, data=data, verify=True)
    if fo.status_code != 200:
        raise Exception(fo.text)
    return fo.text


def check(app_id, app_key, sckey, scvalue):
    """Determine if the captcha was validated.

    :param app_id: your app id (string)
    :param app_key: your app key (string)
    :param sckey: the input value of `sckey` hidden input embedded by us to
    your form (string)
    :param scvalue: the input value of `scvalue` hidden input embedded by us
    to your form (string)
    :return: True if valid, False if not.
    """
    data = dict(app_id=app_id, app_key=app_key, platform='api',
                method='check', sckey=sckey, scvalue=scvalue)
    fo = requests.post(SWEETCAPTCHA_API, data=data, verify=True)
    if fo.status_code != 200:
        raise Exception(fo.text)
    return fo.text


if __name__ == '__main__':
    """For testing a debugging, run this script via the python interpeter.
    First argument is the app_id and the second is the app_key
    Runs with debugging output on to the console.
    """
    import sys
    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    print(get_html(sys.argv[1], sys.argv[2]))

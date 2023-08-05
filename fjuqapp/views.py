from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Teacher

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件

                # 篩選teacher資料表中，teacher欄位中的資料
                teachers = Teacher.objects.filter(name=event.message.text)

                content = ''  # 回覆使用者的內容
                for teacher in teachers:
                        content += f"姓名：{teacher.name}\n"
                        content += f"聯絡方式：{teacher.phone}\n"
                        content += f"辦公室位置：{teacher.office}\n"
                        content += f"信箱：{teacher.email}  "
                    # content += teacher.name + '\n' + teacher.office+ '\n' +teacher.phone+ '\n' + teacher.email + '\n'

                line_bot_api.reply_message(  # 回覆訊息
                    event.reply_token,
                    TextSendMessage(text=content)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()




# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
# from linebot import LineBotApi, WebhookHandler
# from django.views.decorators.csrf import csrf_exempt
# from linebot.models import TextMessage
# from .models import Teacher
# from django.conf import settings

# line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
# handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

# @csrf_exempt
# def callback(request):
#     if request.method == 'POST':
#         # 解析 Line Bot 的輸入訊息
#         signature = request.META['HTTP_X_LINE_SIGNATURE']
#         body = request.body.decode('utf-8')
#         events = handler.parse(body, signature)

#         for event in events:
#             if isinstance(event.message, TextMessage):
#                 user_input = event.message.text
#                 # 在資料庫中查詢相應的資料
#                 teachers = Teacher.objects.filter(name__icontains=event.message.text)
                
#                 reply_message = ''
#                 if teachers.exists():
#                     for teacher in teachers:
#                         reply_message += f"姓名：{teacher.name}\n"
#                         reply_message += f"專長：{teacher.expertise}\n"
#                         reply_message += f"聯絡方式：{teacher.phone}\n"
#                         reply_message += f"辦公室位置：{teacher.office}\n"
#                         reply_message += f"信箱：{teacher.email}\n\n"
#                 else:
#                     reply_message = "抱歉，找不到相關的科系資料。"

#                 # 回覆訊息給 Line Bot
#                 line_bot_api.reply_message(
#                     event.reply_token,
#                     TextMessage(text=reply_message)
#                 )

#         return HttpResponse()

#     else:
#        return HttpResponseBadRequest()
    

# def callback(request):
#     if request.method == 'POST':
#         # 解析 Line Bot 的輸入訊息
#         signature = request.META['HTTP_X_LINE_SIGNATURE']
#         body = request.body.decode('utf-8')
#         events = handler.parse(body, signature)

#         for event in events:
#             if isinstance(event.message, TextMessage):
#                 user_input = event.message.text
#                 # 在資料庫中查詢相應的資料
#                 teachers = Teacher.objects.filter(name__icontains=user_input)
#                 reply_message = ''
#                 if teachers.exists():
#                     for teacher in teachers:
#                         reply_message += f"姓名：{teacher.name}\n"
#                         reply_message += f"專長：{teacher.expertise}\n"
#                         reply_message += f"聯絡方式：{teacher.phone}\n"
#                         reply_message += f"辦公室位置：{teacher.office}\n"
#                         reply_message += f"信箱：{teacher.email}\n\n"
#                 else:
#                     reply_message = "抱歉，找不到相關的科系資料。"

#                 # 回覆訊息給 Line Bot
#                 line_bot_api.reply_message(
#                     event.reply_token,
#                     TextMessage(text=reply_message)
#                 )

#         return HttpResponse()

#     else:
#        return HttpResponseBadRequest()
    # return JsonResponse({"message": "Invalid request method"}, status=405)

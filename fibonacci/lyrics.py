
song = '[00:22.28] চল দোতং পাহাড় জুম ঘরে [00:27.05]পূর্ণিমা রাত বর্ষা জুড়ে জীবন জুয়ার আসর বসাবো! [00:34.53]চল দোতং পাহাড় জুম ঘরে [00:39.04]পূর্ণিমা রাত বর্ষা জুড়ে জীবন জুয়ার আসর বসাবো! [00:46.04]আমি মারফা রেঁধে দেবো পাতে, [00:49.54]বিন্নি চালের ভাত সাথে। [00:53.03]দু বেলা দু মুঠো খেয়ে তৃপ্তির আলিঙ্গন। [00:57.81]পুবের হু হু বাতাস বইলে পরে, পাঁজর ভাঙ্গা গান ধরে [01:04.06]আয়েশ করেই কাটুক এ যৌবন! [01:08.82] চল দোতং পাহাড় জুম ঘরে [01:12.53]পূর্ণিমা রাত বর্ষা জুড়ে জীবন জুয়ার আসর বসাবো! [01:32.53]এই ইটের শহর পোড়ায় খালি, জোড়াতালি জীবন আমার ভাল্লাগেনা রে.... [01:42.81]কে কার রাখে খবর দম ফুরালেও একলা একা নিথর দেহ কাইন্দা মরে রে.... [01:54.80]এই ইটের শহর পোড়ায় খালি, জোড়াতালি জীবন আমার ভাল্লাগেনা রে.... [02:04.54]কে কার রাখে খবর দম ফুরালেও একলা একা নিথর দেহ কাইন্দা মরে রে.... [02:14.53]কে পাইলো কার কি গেলো, কার কি বা আসে যায় [02:22.05]মন ঝিরির পথে হাটার লোভে কেমন করে হায়! [02:28.55]চল দোতং পাহাড় জুম ঘরে [02:31.80]পূর্ণিমা রাত বর্ষা জুড়ে জীবন জুয়ার আসর বসাবো! [02:51.30]এক শেকড় কাটা বৃক্ষ আমি, ডালপালা নাই নতুন পাতাও আর আসেনা রে.... [03:01.28]যে যার নিজের মত ফুল থেকে ফুল সৃষ্টি খেলায় মত্ত আমার ফুল জোটেনা রে... [03:13.54]এক শেকড় কাটা বৃক্ষ আমি, ডালপালা নাই নতুন পাতাও আর আসেনা রে.... [03:23.54]যে যার নিজের মত ফুল থেকে ফুল সৃষ্টি খেলায় মত্ত আমার ফুল জোটেনা রে... [03:35.53]এই ছোট্ট জীবন স্বপ্ন যেমন কিসের তরে হায় ! [03:41.32]তাই জটিল ধাঁধার শহর ছেড়ে মন পাহাড়েই যায় [03:47.55]চল দোতং পাহাড় জুম ঘরে [03:52.29]পূর্ণিমা রাত বর্ষা জুড়ে জীবন জুয়ার আসর বসাবো! [03:58.81]চল দোতং পাহাড় জুম ঘরে [04:02.05]পূর্ণিমা রাত বর্ষা জুড়ে জীবন জুয়ার আসর বসাবো! [04:09.53]আমি মারফা রেঁধে দেবো পাতে, [04:14.53]বিন্নি চালের ভাত সাথে। [04:16.53]দু বেলা দু মুঠো খেয়ে তৃপ্তির আলিঙ্গন। [04:21.56]পুবের হু হু বাতাস বইলে পরে, পাঁজর ভাঙ্গা গান ধরে [04:27.55]আয়েশ করেই কাটুক এ যৌবন! [04:32.04] চল দোতং পাহাড় জুম ঘরে [04:35.54]পূর্ণিমা রাত বর্ষা জুড়ে জীবন জুয়ার আসর বসাবো!'
# full_timer = []
# for m in range(5):
#     for s in range(61):
#         for ms in range(61):
#             if len(str(ms))==1:
#                 ms = f"0{ms}"
#             if len(str(s))==1:
#                 s = f"0{s}"
#             full_timer.append(f"0{m}:{s}.{ms}")
#
# time = []
# for i in full_timer:
#     if i in song:
#         time.append(f"{i}")
#
# lyrics = [song]
# x=0
with open("lyrics.txt","w", encoding="utf-8") as file:
    my_list = song.split("[")

    for i in my_list:
        line = i[9:].strip()
        file.write(line+"\n")








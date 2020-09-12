import pyautogui#Terminal မှာ Package install လုပ် (pip install pyautogui)
import time#အချိန်မထည့်ထားရင် တစက္ကန့်ကို စာအများကြီးဆိုရင် ဖေ့ဘုတ်က ဘန်းမှာစိုးလို့
#(စိတ်မပူနဲ့ အခုမဘန်းအောင်ရေးပေးထားတယ် အာမခံတယ်)

cmt = ["Yeah,I  am working", "I am Jack's bot","Thank Jack For Creating Me", "Hello,I am Jack.I am testing my Python Bot", "Success", "Bot commenting Radom String That I Enter", "Just for fun"]#ကိုယ်ပေါ်ချင်တဲ့စာကိုယ်ပြောင်းထည့်ရတယ် အရေအတွက်တော့မှတ်ထား အခုဝော့ 7 ခုထည့်ပေးထားတယ်
time.sleep(1)#လူဆန်အောင်အချိန်ဆွဲတာ

#အကြောင်းရေတ‌စ်ထောင်ထုတိပြချင်လို့ loop ပတ်မယ်
for i in range(1000): 
    pyautogui.typewrite(cmt[i%7])#Cmt ဆိုတဲ့ array မှာ 7 ခုထည့်ပေးထားလို့ %7 ဖြစ်တာ ကိုက 2 ခုဘဲထည့်ရင် %2 ပေါ့ အဲတာမှမသ်ရင်တော့ ဘာမှမလုပ်တာပိုကောင်းမယ်
    pyautogui.typewrite("\n")#Facebook က enter ခေါ်မှ ကွန်မန့်တစ်ကြောင့် မန့်တာမလို့ enter ခေါက်ခိုင်းဝာ
    time.sleep(2)#လူဆန်အောင်အချိန်ဆွဲတာ
    
#Guide pdf ဖတ်ပြီးမှ run ပါ ခင်ဗျ
#nay kaung lar!,

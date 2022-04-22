from django.contrib import admin
from emailapp.models import login,signUp,sendMsg,receiveMsg,setContacts,getprofileData,usersLog,walletBalance


admin.site.register(login)
admin.site.register(signUp)
admin.site.register(sendMsg)
admin.site.register(receiveMsg)
admin.site.register(setContacts)
admin.site.register(getprofileData)
admin.site.register(usersLog)
admin.site.register(walletBalance)

# Register your models here.

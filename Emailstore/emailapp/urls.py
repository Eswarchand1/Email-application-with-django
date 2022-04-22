from django.urls import path
from . import views

# . means current project import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


app_name='email'

urlpatterns=[
    #path('',views.loginPageView.as_view(),name='index'),
    #path('home',views.homePageView.as_view(),name='home'),
    path('home',views.homePage,name='home'),
    path('gd',views.getdata, name="gd"),
    path('signup', views.signUp, name="signup"),
    path('data',views.show_data, name="data"),
    path('search', views.sum1, name="search"),
    path('sd', views.searchMails, name='sd'),
    path('getdata',views.SearchResultsView,name='getdata'),
    path('home1',views.SearchHome, name="home1"),
    path('profile',views.profilePage,name="profile"),
    path('updateprofile',views.updateProfile,name="updateprofile"),
    #path('profile/<int:pk>',views.showProfile.as_view(),name="profile"),
    path('displayprofile',views.displayProfile,name="displayprofile"),
    path('displayfullcontact',views.fullContact,name="displayfullcontact"),
    path('forgotmail',views.forgotMail,name="forgotmail"),
    path('forgotpass', views.forgotPassword, name="forgotpass"),
    path('contacts', views.contactsPage, name="contacts"),
    path('addcontacts', views.addcontactsPage, name="addcontacts"),
    path('deletecontacts', views.deletecontactsPage, name="deletecontacts"),
    path('updatecontacts', views.updatecontactsPage, name="updatecontacts"),
    path('displaycontacts', views.displaycontactsPage, name="displaycontacts"),
    path('uploadfile', views.uploadFile, name="uploadfile"),
    path('homesearch',views.homeSearch,name="homesearch"),
    path('userlogs', views.userLogPage, name="userlogs"),
    path('sendedmails', views.sendedMessages, name="sendedmails"),
    path('wallet', views.wallerPage, name="wallet"),
    path('loggedout', views.loggedOutPage, name="loggedout"),
    path('retry', views.retryPage, name="retry"),
    path('walletBalance', views.addWalletBal, name="walletBalance"),


    path('',views.login,name='index'),


]
urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
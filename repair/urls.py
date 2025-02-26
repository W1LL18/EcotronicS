from django.urls import path
from . import views

handler404 = 'repair.views.custom_404'
    
app_name = 'repair'

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("faq/",views.faq,name="faq"),
    path("login/",views.login_user,name="login"),
    path("terms/",views.terms,name="terms"),
    path("blog/",views.blog,name="blog"),
    path('category/<int:id>/', views.category, name='category'),
    path('category/blog-post/<int:id>/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.custom_logout, name='logout'),
    path('admin-page/',views.admin_page, name='admin'),
    path('admin-page/about-edit',views.about_edit, name='about_edit'),
    path('admin-page/faq-edit',views.sup_edit, name='faq_edit'),
    path('admin-page/user-edit',views.user_edit, name='user_edit'),
    path('admin-page/order',views.book, name='book'),
    path('admin-page/apply',views.com, name='apply'),
    path('admin-page/new',views.new, name='new'),
    path('admin-page/blog/post',views.blogpost, name='blogpost'),
    path('admin-page/setting',views.setting, name='setting'),
    path('admin-page/blog/category',views.cat_edit, name='cat_edit'),
    path('admin-page/profile',views.admin_profile,name='admin_profile'),
    path('register/',views.register_user,name='register'),
    path('register/personal-data/',views.register_user2,name='register2'),
    path('admin-page/brand',views.brand,name='brand'),
    path('admin-page/model/<int:id>/',views.model,name='model'),
    path('admin-page/model/',views.model2,name='modelm'),
    path('admin-page/model/add/',views.modeladd,name='modeladd'),
    path('admin-page/problem/',views.problem2,name='problemm'),
    path('admin-page/problem/<int:id>/',views.problem,name='problem'),
    path('admin-page/problem/add/',views.problemadd,name='problemadd'),
    path('admin-page/price',views.price2,name='pricem'),
    path('admin-page/price/<int:id>/',views.price,name='price'),
    path('admin-page/price/add/',views.priceadd,name='priceadd'),
]



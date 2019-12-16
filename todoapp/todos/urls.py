from django.urls import path
from todos.views import TodoListCreateAPIView, TodoDetailAPIView

app_name = 'todos'

urlpatterns = [
    path('', TodoListCreateAPIView.as_view(), name="list"),#point the URL to the as_view() class method instead,
    # which provides a function-like entry to class-based views
    path('<int:pk>/', TodoDetailAPIView.as_view(), name="detail"),#namespace of int, url of pk
]#<> capturs value of url, int is a converter type, if it wasn't there, any string would be matched.
#int Matches zero or any positive integer. Returns an int.
#in detail, use whatever num value was captured.


#.as_view() no state is held by the View class between one request and the next. If Django didn’t
# do this, you’d need to be excessively careful that you didn’t assign to some member of the view
# that would lead to different behaviour next time the view was run

#In Class-based views, you have to call as_view() function so as to return a callable view that
#takes a request and returns a response. Its the main entry-point in request-response cycle in
#case of generic views.
#You just can't use class-based views like you could in normal function-based views.
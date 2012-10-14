from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from meetings.views import (PastMeetings,
                            ProposeTopic,
                            MyTopics,
)

urlpatterns = patterns("",
    url(r'^past/$', PastMeetings.as_view(), name='past_meetings'),
    url(r'^topics/propose$', login_required(ProposeTopic.as_view()), name='propose_topic'),
    url(r'^topics/mine$', login_required(MyTopics.as_view()), name='my_topics'),
)

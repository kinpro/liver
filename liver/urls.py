
from django.conf.urls import *


urlpatterns = patterns('liver.views',
        (r'^api/external/get_worker_jobs$',
        'api_external_get_worker_jobs',
        None, 'api-external-get-worker-jobs'),
        (r'^api/external/notify_worker_jobs_result$',
        'api_external_notify_worker_jobs_result',
        None, 'api-external-notify-worker-jobs-result'),

)

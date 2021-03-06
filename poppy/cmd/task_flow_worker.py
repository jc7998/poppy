# Copyright (c) 2014 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import socket

from oslo_config import cfg

from poppy import bootstrap
from poppy.openstack.common import log


LOG = log.getLogger(__name__)


def run():
    conf = cfg.CONF
    conf(project='poppy', prog='poppy', args=[])
    conductor_name = '{0}-{1}'.format(socket.gethostname(), os.getpid())
    b = bootstrap.Bootstrap(conf)
    b.distributed_task.services_controller.run_task_worker(name=conductor_name)

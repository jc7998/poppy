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

from oslo_config import cfg
from taskflow.patterns import linear_flow

from poppy.distributed_task.taskflow.task import update_service_state_tasks
from poppy.openstack.common import log


LOG = log.getLogger(__name__)


conf = cfg.CONF
conf(project='poppy', prog='poppy', args=[])


def disable_service():
    flow = linear_flow.Flow('Disable service').add(
        update_service_state_tasks.UpdateServiceStateTask(),
        update_service_state_tasks.BreakDNSChainTask()
    )
    return flow


def enable_service():
    flow = linear_flow.Flow('Enable service').add(
        update_service_state_tasks.UpdateServiceStateTask(),
        update_service_state_tasks.FixDNSChainTask()
    )
    return flow

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp
import logging

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICGenerator()

v1_library = gapic.ruby_library(
    'datastore', 'v1',
    config_path='/google/datastore/artman_datastore.yaml',
    artman_output_name='google-cloud-ruby/google-cloud-datastore'
)
s.copy(v1_library / 'lib/google/cloud/datastore/v1')
s.copy(v1_library / 'lib/google/datastore/v1')

# Omitting lib/google/cloud/datastore/v1.rb for now because we are not exposing
# the low-level API.

# https://github.com/googleapis/gapic-generator/issues/2124
s.replace(
    'lib/google/cloud/datastore/v1/credentials.rb',
    'SCOPE = \[[^\]]+\]\.freeze',
    'SCOPE = ["https://www.googleapis.com/auth/datastore"].freeze')

# https://github.com/googleapis/gapic-generator/issues/2243
s.replace(
    'lib/google/cloud/datastore/v1/*_client.rb',
    '(\n\\s+class \\w+Client\n)(\\s+)(attr_reader :\\w+_stub)',
    '\\1\\2# @private\n\\2\\3')